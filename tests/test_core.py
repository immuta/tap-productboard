"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_productboardapi.tap import TapProductboardAPI


SAMPLE_CONFIG = {
    "api_key": "eyJ0eXAiOiJKV1QiLCJraWQiOiJhNDljZmViMmE3MmIyOTEzNzc1YTdjZDE4YzEyNmQxN2FjZjJiZjU0OWIzZTMxOGE4ZDgwZjk0NDhkZjlkYWU3IiwiYWxnIjoiUlM1MTIifQ.eyJpYXQiOjE2Nzg0NzQ3NTEsImlzcyI6IjA5ZWI0ZjA3LWMwNTItNGFhYy04MzhlLTExMjY5ZTlhNmNlOCIsInN1YiI6IjYzOTc2MyIsInJvbGUiOiJhZG1pbiIsImF1ZCI6Imh0dHBzOi8vYXBpLnByb2R1Y3Rib2FyZC5jb20iLCJ1c2VyX2lkIjo2Mzk3NjMsInNwYWNlX2lkIjoiMTQxOTcyIn0.U05bRQ6xcI-wKGCnXcpxtDa5tjj0VNfmPdsMScG6DYnTf-aG6WiA6PZ06qku4i8U9vy4Apy0ARulv2BKg0y-ok2g542kKktUOlFEQEdKbaUhhktknUb2Kw99HFWIUkGhle0EiHBTs5LxJUMruQVEkHiJxyGjSTN_PgVJK7xnD1zaQZMMNGY5QvkbFr3lVHLHcyrJZROFl7iwcQBsDFZAcJKPGAOtQjOSlpmL60BwFAHhwFT4upeTw-AYr3yavAQwjK_ubQBE4JvrzKLy2SKw2chbwi0s_IMu0fRjld3oqcrpE7E9LeLrh9IvmTjmkPutdFvnIL5-QFprCAohPMhw0w",
    "X-Version": "1"
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    TestTapProductboardAPI = get_standard_tap_tests(
        tap_class=TapProductboardAPI,
        config=SAMPLE_CONFIG
    )
    for test in TestTapProductboardAPI:
        test()


# TODO: Create additional tests as appropriate for your tap.
