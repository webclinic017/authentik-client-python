# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.6.1
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class LDAPAPIAccessMode(str, Enum):
    """
    * `direct` - Direct * `cached` - Cached
    """

    """
    allowed enum values
    """
    DIRECT = 'direct'
    CACHED = 'cached'

    @classmethod
    def from_json(cls, json_str: str) -> LDAPAPIAccessMode:
        """Create an instance of LDAPAPIAccessMode from a JSON string"""
        return LDAPAPIAccessMode(json.loads(json_str))


