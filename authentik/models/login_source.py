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
from pydantic import BaseModel, Field, StrictStr
from authentik.models.login_challenge_types import LoginChallengeTypes

class LoginSource(BaseModel):
    """
    Serializer for Login buttons of sources
    """
    name: StrictStr = Field(...)
    icon_url: Optional[StrictStr] = None
    challenge: LoginChallengeTypes = Field(...)
    __properties = ["name", "icon_url", "challenge"]

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
    def from_json(cls, json_str: str) -> LoginSource:
        """Create an instance of LoginSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of challenge
        if self.challenge:
            _dict['challenge'] = self.challenge.to_dict()
        # set to None if icon_url (nullable) is None
        # and __fields_set__ contains the field
        if self.icon_url is None and "icon_url" in self.__fields_set__:
            _dict['icon_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginSource:
        """Create an instance of LoginSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoginSource.parse_obj(obj)

        _obj = LoginSource.parse_obj({
            "name": obj.get("name"),
            "icon_url": obj.get("icon_url"),
            "challenge": LoginChallengeTypes.from_dict(obj.get("challenge")) if obj.get("challenge") is not None else None
        })
        return _obj


