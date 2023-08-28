# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.6.1
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, constr

class OAuthDeviceCodeChallengeResponseRequest(BaseModel):
    """
    Response that includes the user-entered device code
    """
    component: Optional[constr(strict=True, min_length=1)] = 'ak-provider-oauth2-device-code'
    code: StrictInt = Field(...)
    __properties = ["component", "code"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OAuthDeviceCodeChallengeResponseRequest:
        """Create an instance of OAuthDeviceCodeChallengeResponseRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthDeviceCodeChallengeResponseRequest:
        """Create an instance of OAuthDeviceCodeChallengeResponseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthDeviceCodeChallengeResponseRequest.parse_obj(obj)

        _obj = OAuthDeviceCodeChallengeResponseRequest.parse_obj({
            "component": obj.get("component") if obj.get("component") is not None else 'ak-provider-oauth2-device-code',
            "code": obj.get("code")
        })
        return _obj


