"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetUsersResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_users_200_application_json_strings: Optional[list[str]] = dataclasses.field(default=None)
    r"""A JSON array of user names"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    