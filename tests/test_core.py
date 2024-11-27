"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_productboardapi.tap import TapProductboardAPI


SAMPLE_CONFIG = {
    "api_key": "",
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
