from nose.plugins.attrib import attr

from ..data import *

from libs.api.api_client import APIClient



class TestLogin():
    """
    If the app had included a JSON/HTTP component, I would use a process
    similar to the one below to test the API endpoint responses using
    all possible (reasonable) combinations of inputs, HTTP methods, etc.
    per endpoint in a black-box fashion.

    """

    def setup(self):
        self.client = APIClient()

    def test_get_baseurl_returns_200(self):
        data = {}
        request = self.client.make_request('GET', BASEURL, data)

        assert 200 in (request.status_code, )
