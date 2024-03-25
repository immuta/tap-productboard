"""REST client handling, including ProductboardAPIStream base class."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Union, List, Iterable, Callable, Iterable

import requests
import re
from singer_sdk.authenticators import BearerTokenAuthenticator, APIAuthenticatorBase
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import SimpleAuthenticator
from singer_sdk.pagination import BaseHATEOASPaginator
from singer_sdk.pagination import BaseAPIPaginator

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

#streamDetect = ''
class ProductboardAPIStream(RESTStream):
    """ProductboardAPI stream class."""

    # TODO: Set the API's base URL here:
    url_base = "https://api.productboard.com"

    # OR use a dynamic url_base:
    #@property
    #def url_base(self) -> str:
     #   print("url check:", self.config["api_url"])
    #     """Return the API URL root, configurable via tap settings."""
      #  return self.config["api_url"]

    records_jsonpath = "$.data[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.links.next"  # Or override `get_next_page_token`.
    next_page_token_notes_jsonpath = "$.pageCursor"  # Or override `get_next_page_token`.
    #global streamDetect = ''

    #def __init__(self, streamDetect):
    #    self.streamDetect = streamDetect
    
    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        headers["Authorization"] = "Bearer " + self.config.get("api_key").strip()
        headers["X-Version"] = self.config.get("X-Version")
        #headers["pageLimit"] = self.config.get("pageLimit")
        return headers

    def get_next_page_token(
        self,
        response: requests.Response,
        previous_token: Any | None,
    ) -> Any | None:
        """Return a token for identifying next page or None if no more pages.

        Args:
            response: The HTTP ``requests.Response`` object.
            previous_token: The previous page token value.

        Returns:
            The next pagination token.
        """
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        all_matches = extract_jsonpath(
            self.next_page_token_jsonpath, response.json()
        )
        first_match = next(iter(all_matches), None)
        #print("first feature match", first_match)
        #print("keys", response.json().keys())
        #global streamDetect
        if first_match:
            next_page_token = first_match
            #print("class name", self)
            #streamDetect = 'feature'
        #if "pageCursor" in response.json().keys():
            #print("test if statement")
            #next_page_token = response.json()['pageCursor']
        #else:
            #notes_token = "$.pageCursor"
            #print("token", response.json().keys())
        
        else:
            if "pageCursor" in response.json().keys():
                all_notes_matches = extract_jsonpath(
                    self.next_page_token_notes_jsonpath, response.json()
                )
                next_page_token = next(iter(all_notes_matches), None)
                #next_page_token = response.json().pageCursor
                #print("check token 1", next_page_token)
                #print("class name", self.name)
                #next_page_token = next_page_token.replace("=","%3D", 1)
                #streamDetect = 'note'
            else:
                next_page_token = None
            #next_page_token = response.json()['pageCursor']
            #next_page_token = response.headers.get("X-Next-Page", None)
            #print("check token 2", next_page_token)
            #streamDetect = 'note'
        #if next_page_token and next_page_token == self._value:
        #    self._value = 'override next page token'
        #runtimeCounter = runtimeCounter + 1
        #if runtimeCounter > 3:
        #    exit
        return next_page_token

    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        #print("next page token", next_page_token)
        if next_page_token:
            param_match = re.search("pageCursor=([^&]*)", next_page_token)
            if param_match:
                pageCursormatch = param_match.group(1)
            else:
                #print("got here")
                pageCursormatch = next_page_token
                #print("got here 2")
            params["pageCursor"] = pageCursormatch
            #print("parameter", pageCursormatch)
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        #print("got here") 
        #print('stream Detect', streamDetect)
        #if self.name == 'note':
        #    params["pageLimit"] = '2000'
        if self.name == 'text_custom_fields' or self.name == 'text_custom_field_names':
            params["type"] = 'text'
        if self.name == 'custom_description_custom_fields' or self.name == 'custom_description_custom_field_names':
            params["type"] = 'custom-description'
        if self.name == 'number_custom_fields' or self.name == 'number_custom_field_names':
            params["type"] = 'number'
        if self.name == 'dropdown_custom_fields' or self.name == 'dropdown_custom_field_names':
            params["type"] = 'dropdown'
        if self.name == 'multi_dropdown_custom_fields' or self.name == 'multi_dropdown_custom_field_names':
            params["type"] = 'multi-dropdown'
        if self.name == 'member_custom_fields' or self.name == 'member_custom_field_names':
            params["type"] = 'member'
        return params

    #def prepare_request_payload(
    #    self,
    #    context: dict | None,
    #    next_page_token: Any | None,
    #) -> dict | None:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary with the JSON body for a POST requests.
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
    #    return None

    #def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # TODO: Parse response body and return a set of records.
    #    yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    #def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        # TODO: Delete this method if not needed.
    #    return row
