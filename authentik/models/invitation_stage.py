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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from authentik.models.flow_set import FlowSet

class InvitationStage(BaseModel):
    """
    InvitationStage Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    component: StrictStr = Field(..., description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    flow_set: Optional[conlist(FlowSet)] = None
    continue_flow_without_invitation: Optional[StrictBool] = Field(None, description="If this flag is set, this Stage will jump to the next Stage when no Invitation is given. By default this Stage will cancel the Flow when no invitation is given.")
    __properties = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "continue_flow_without_invitation"]

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
    def from_json(cls, json_str: str) -> InvitationStage:
        """Create an instance of InvitationStage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "component",
                            "verbose_name",
                            "verbose_name_plural",
                            "meta_model_name",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvitationStage:
        """Create an instance of InvitationStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvitationStage.parse_obj(obj)

        _obj = InvitationStage.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "continue_flow_without_invitation": obj.get("continue_flow_without_invitation")
        })
        return _obj


