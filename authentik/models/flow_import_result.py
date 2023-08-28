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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictBool, conlist

class FlowImportResult(BaseModel):
    """
    Logs of an attempted flow import
    """
    logs: conlist(Dict[str, Any]) = Field(...)
    success: StrictBool = Field(...)
    __properties = ["logs", "success"]

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
    def from_json(cls, json_str: str) -> FlowImportResult:
        """Create an instance of FlowImportResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "logs",
                            "success",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlowImportResult:
        """Create an instance of FlowImportResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlowImportResult.parse_obj(obj)

        _obj = FlowImportResult.parse_obj({
            "logs": obj.get("logs"),
            "success": obj.get("success")
        })
        return _obj


