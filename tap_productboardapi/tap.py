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
            default="Bearer eyJ0eXAiOiJKV1QiLCJraWQiOiJhNDljZmViMmE3MmIyOTEzNzc1YTdjZDE4YzEyNmQxN2FjZjJiZjU0OWIzZTMxOGE4ZDgwZjk0NDhkZjlkYWU3IiwiYWxnIjoiUlM1MTIifQ.eyJpYXQiOjE2Nzg0NzQ3NTEsImlzcyI6IjA5ZWI0ZjA3LWMwNTItNGFhYy04MzhlLTExMjY5ZTlhNmNlOCIsInN1YiI6IjYzOTc2MyIsInJvbGUiOiJhZG1pbiIsImF1ZCI6Imh0dHBzOi8vYXBpLnByb2R1Y3Rib2FyZC5jb20iLCJ1c2VyX2lkIjo2Mzk3NjMsInNwYWNlX2lkIjoiMTQxOTcyIn0.U05bRQ6xcI-wKGCnXcpxtDa5tjj0VNfmPdsMScG6DYnTf-aG6WiA6PZ06qku4i8U9vy4Apy0ARulv2BKg0y-ok2g542kKktUOlFEQEdKbaUhhktknUb2Kw99HFWIUkGhle0EiHBTs5LxJUMruQVEkHiJxyGjSTN_PgVJK7xnD1zaQZMMNGY5QvkbFr3lVHLHcyrJZROFl7iwcQBsDFZAcJKPGAOtQjOSlpmL60BwFAHhwFT4upeTw-AYr3yavAQwjK_ubQBE4JvrzKLy2SKw2chbwi0s_IMu0fRjld3oqcrpE7E9LeLrh9IvmTjmkPutdFvnIL5-QFprCAohPMhw0w",
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
            streams.NoteStream(self)
        ]


if __name__ == "__main__":
    TapProductboardAPI.cli()
