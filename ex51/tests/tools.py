from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):
    assert status in resp.status, f"Expected {status}, got {resp.status}"
    if contains:
        assert contains in resp.data, f"Did not find '{contains}' in {resp.data}"
    if matches:
        reg = re.compile(matches)
        assert reg.search(resp.data), f"'{matches}' did not match {resp.data}"
    if headers:
        assert_equal(resp.headers, headers)
