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





class AuthTypeEnum(str, Enum):
    """
    * `basic` - Basic * `bearer` - Bearer
    """

    """
    allowed enum values
    """
    BASIC = 'basic'
    BEARER = 'bearer'

    @classmethod
    def from_json(cls, json_str: str) -> AuthTypeEnum:
        """Create an instance of AuthTypeEnum from a JSON string"""
        return AuthTypeEnum(json.loads(json_str))


