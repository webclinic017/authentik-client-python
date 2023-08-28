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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from authentik.models.flow_set_request import FlowSetRequest
from authentik.models.user_creation_mode_enum import UserCreationModeEnum

class PatchedUserWriteStageRequest(BaseModel):
    """
    UserWriteStage Serializer
    """
    name: Optional[constr(strict=True, min_length=1)] = None
    flow_set: Optional[conlist(FlowSetRequest)] = None
    user_creation_mode: Optional[UserCreationModeEnum] = None
    create_users_as_inactive: Optional[StrictBool] = Field(None, description="When set, newly created users are inactive and cannot login.")
    create_users_group: Optional[StrictStr] = Field(None, description="Optionally add newly created users to this group.")
    user_path_template: Optional[StrictStr] = None
    __properties = ["name", "flow_set", "user_creation_mode", "create_users_as_inactive", "create_users_group", "user_path_template"]

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
    def from_json(cls, json_str: str) -> PatchedUserWriteStageRequest:
        """Create an instance of PatchedUserWriteStageRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        # set to None if create_users_group (nullable) is None
        # and __fields_set__ contains the field
        if self.create_users_group is None and "create_users_group" in self.__fields_set__:
            _dict['create_users_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedUserWriteStageRequest:
        """Create an instance of PatchedUserWriteStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedUserWriteStageRequest.parse_obj(obj)

        _obj = PatchedUserWriteStageRequest.parse_obj({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "user_creation_mode": obj.get("user_creation_mode"),
            "create_users_as_inactive": obj.get("create_users_as_inactive"),
            "create_users_group": obj.get("create_users_group"),
            "user_path_template": obj.get("user_path_template")
        })
        return _obj


