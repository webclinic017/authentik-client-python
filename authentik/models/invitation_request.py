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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class InvitationRequest(BaseModel):
    """
    Invitation Serializer
    """
    name: constr(strict=True, max_length=50, min_length=1) = Field(...)
    expires: Optional[datetime] = None
    fixed_data: Optional[Dict[str, Any]] = None
    single_use: Optional[StrictBool] = Field(None, description="When enabled, the invitation will be deleted after usage.")
    flow: Optional[StrictStr] = Field(None, description="When set, only the configured flow can use this invitation.")
    __properties = ["name", "expires", "fixed_data", "single_use", "flow"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
    def from_json(cls, json_str: str) -> InvitationRequest:
        """Create an instance of InvitationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if flow (nullable) is None
        # and __fields_set__ contains the field
        if self.flow is None and "flow" in self.__fields_set__:
            _dict['flow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvitationRequest:
        """Create an instance of InvitationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvitationRequest.parse_obj(obj)

        _obj = InvitationRequest.parse_obj({
            "name": obj.get("name"),
            "expires": obj.get("expires"),
            "fixed_data": obj.get("fixed_data"),
            "single_use": obj.get("single_use"),
            "flow": obj.get("flow")
        })
        return _obj


