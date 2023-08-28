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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr
from authentik.models.prompt_type_enum import PromptTypeEnum
from authentik.models.stage_request import StageRequest

class PromptRequest(BaseModel):
    """
    Prompt Serializer
    """
    name: constr(strict=True, min_length=1) = Field(...)
    field_key: constr(strict=True, min_length=1) = Field(..., description="Name of the form field, also used to store the value")
    label: constr(strict=True, min_length=1) = Field(...)
    type: PromptTypeEnum = Field(...)
    required: Optional[StrictBool] = None
    placeholder: Optional[StrictStr] = Field(None, description="Optionally provide a short hint that describes the expected input value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple choices.")
    initial_value: Optional[StrictStr] = Field(None, description="Optionally pre-fill the input with an initial value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple default choices.")
    order: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = None
    promptstage_set: Optional[conlist(StageRequest)] = None
    sub_text: Optional[StrictStr] = None
    placeholder_expression: Optional[StrictBool] = None
    initial_value_expression: Optional[StrictBool] = None
    __properties = ["name", "field_key", "label", "type", "required", "placeholder", "initial_value", "order", "promptstage_set", "sub_text", "placeholder_expression", "initial_value_expression"]

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
    def from_json(cls, json_str: str) -> PromptRequest:
        """Create an instance of PromptRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in promptstage_set (list)
        _items = []
        if self.promptstage_set:
            for _item in self.promptstage_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['promptstage_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PromptRequest:
        """Create an instance of PromptRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PromptRequest.parse_obj(obj)

        _obj = PromptRequest.parse_obj({
            "name": obj.get("name"),
            "field_key": obj.get("field_key"),
            "label": obj.get("label"),
            "type": obj.get("type"),
            "required": obj.get("required"),
            "placeholder": obj.get("placeholder"),
            "initial_value": obj.get("initial_value"),
            "order": obj.get("order"),
            "promptstage_set": [StageRequest.from_dict(_item) for _item in obj.get("promptstage_set")] if obj.get("promptstage_set") is not None else None,
            "sub_text": obj.get("sub_text"),
            "placeholder_expression": obj.get("placeholder_expression"),
            "initial_value_expression": obj.get("initial_value_expression")
        })
        return _obj


