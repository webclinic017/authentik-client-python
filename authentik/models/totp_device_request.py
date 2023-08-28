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



from pydantic import BaseModel, Field, constr

class TOTPDeviceRequest(BaseModel):
    """
    Serializer for totp authenticator devices
    """
    name: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The human-readable name of this device.")
    __properties = ["name"]

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
    def from_json(cls, json_str: str) -> TOTPDeviceRequest:
        """Create an instance of TOTPDeviceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TOTPDeviceRequest:
        """Create an instance of TOTPDeviceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TOTPDeviceRequest.parse_obj(obj)

        _obj = TOTPDeviceRequest.parse_obj({
            "name": obj.get("name")
        })
        return _obj


