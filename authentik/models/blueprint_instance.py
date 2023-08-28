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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from authentik.models.blueprint_instance_status_enum import BlueprintInstanceStatusEnum

class BlueprintInstance(BaseModel):
    """
    Info about a single blueprint instance file
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    path: Optional[StrictStr] = ''
    context: Optional[Dict[str, Any]] = None
    last_applied: datetime = Field(...)
    last_applied_hash: StrictStr = Field(...)
    status: BlueprintInstanceStatusEnum = Field(...)
    enabled: Optional[StrictBool] = None
    managed_models: conlist(StrictStr) = Field(...)
    metadata: Dict[str, Any] = Field(...)
    content: Optional[StrictStr] = None
    __properties = ["pk", "name", "path", "context", "last_applied", "last_applied_hash", "status", "enabled", "managed_models", "metadata", "content"]

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
    def from_json(cls, json_str: str) -> BlueprintInstance:
        """Create an instance of BlueprintInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "last_applied",
                            "last_applied_hash",
                            "status",
                            "managed_models",
                            "metadata",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlueprintInstance:
        """Create an instance of BlueprintInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlueprintInstance.parse_obj(obj)

        _obj = BlueprintInstance.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "path": obj.get("path") if obj.get("path") is not None else '',
            "context": obj.get("context"),
            "last_applied": obj.get("last_applied"),
            "last_applied_hash": obj.get("last_applied_hash"),
            "status": obj.get("status"),
            "enabled": obj.get("enabled"),
            "managed_models": obj.get("managed_models"),
            "metadata": obj.get("metadata"),
            "content": obj.get("content")
        })
        return _obj


