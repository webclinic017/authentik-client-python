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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, constr, validator
from authentik.models.authentication_enum import AuthenticationEnum
from authentik.models.denied_action_enum import DeniedActionEnum
from authentik.models.flow_designation_enum import FlowDesignationEnum
from authentik.models.layout_enum import LayoutEnum
from authentik.models.policy_engine_mode import PolicyEngineMode

class Flow(BaseModel):
    """
    Flow Serializer
    """
    pk: StrictStr = Field(...)
    policybindingmodel_ptr_id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    slug: constr(strict=True, max_length=50) = Field(..., description="Visible in the URL.")
    title: StrictStr = Field(..., description="Shown as the Title in Flow pages.")
    designation: FlowDesignationEnum = Field(...)
    background: StrictStr = Field(..., description="Get the URL to the background image. If the name is /static or starts with http it is returned as-is")
    stages: conlist(StrictStr) = Field(...)
    policies: conlist(StrictStr) = Field(...)
    cache_count: StrictInt = Field(..., description="Get count of cached flows")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    compatibility_mode: Optional[StrictBool] = Field(None, description="Enable compatibility mode, increases compatibility with password managers on mobile devices.")
    export_url: StrictStr = Field(..., description="Get export URL for flow")
    layout: Optional[LayoutEnum] = None
    denied_action: Optional[DeniedActionEnum] = None
    authentication: Optional[AuthenticationEnum] = None
    __properties = ["pk", "policybindingmodel_ptr_id", "name", "slug", "title", "designation", "background", "stages", "policies", "cache_count", "policy_engine_mode", "compatibility_mode", "export_url", "layout", "denied_action", "authentication"]

    @validator('slug')
    def slug_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> Flow:
        """Create an instance of Flow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "policybindingmodel_ptr_id",
                            "background",
                            "stages",
                            "policies",
                            "cache_count",
                            "export_url",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Flow:
        """Create an instance of Flow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Flow.parse_obj(obj)

        _obj = Flow.parse_obj({
            "pk": obj.get("pk"),
            "policybindingmodel_ptr_id": obj.get("policybindingmodel_ptr_id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "title": obj.get("title"),
            "designation": obj.get("designation"),
            "background": obj.get("background"),
            "stages": obj.get("stages"),
            "policies": obj.get("policies"),
            "cache_count": obj.get("cache_count"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "compatibility_mode": obj.get("compatibility_mode"),
            "export_url": obj.get("export_url"),
            "layout": obj.get("layout"),
            "denied_action": obj.get("denied_action"),
            "authentication": obj.get("authentication")
        })
        return _obj


