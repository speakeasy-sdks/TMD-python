"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Optional

SERVERS = [
    "http://api.example.com/v1",
    r"""Optional server description, e.g. Main (production) server"""
    "http://staging-api.example.com",
    r"""Optional server description, e.g. Internal staging server for testing"""
]
"""Contains the list of servers available to the SDK"""

class SDK:
    r"""Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.1.3"
    _gen_version: str = "2.26.3"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        
    
    
    
    def get_users(self) -> operations.GetUsersResponse:
        r"""Returns a list of users.
        Optional extended description in CommonMark or HTML.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/users'
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUsersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[str]])
                res.get_users_200_application_json_strings = out

        return res

    