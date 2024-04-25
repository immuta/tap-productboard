"""ProductboardAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_productboardapi import streams


class TapProductboardAPI(Tap):
    """ProductboardAPI tap class."""

    name = "tap-productboardapi"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "X-Version",
            th.StringType,
            required=True,
            default="1",
            description="API Version Header Parameter",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.productboard.com",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.ProductboardAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.FeatureStream(self),
            streams.FeatureStatusStream(self),
            streams.TextCustomFieldsStream(self),
            streams.CustomDescriptionCustomFieldsStream(self),
            streams.NumberCustomFieldsStream(self),
            streams.DropdownCustomFieldsStream(self),
            streams.MultiDropdownCustomFieldsStream(self),
            streams.MemberCustomFieldsStream(self),
            streams.MemberCustomFieldNamesStream(self),
            streams.MultiDropdownCustomFieldNamesStream(self),
            streams.DropdownCustomFieldNamesStream(self),
            streams.NumberCustomFieldNamesStream(self),
            streams.CustomDescriptionCustomFieldNamesStream(self),
            streams.TextCustomFieldNamesStream(self),
            streams.NoteStream(self),
            streams.UserStream(self),
            streams.CompanyStream(self)
        ]


if __name__ == "__main__":
    TapProductboardAPI.cli()
