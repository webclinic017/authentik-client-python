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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from authentik.models.outpost_type_enum import OutpostTypeEnum
from authentik.models.provider import Provider
from authentik.models.service_connection import ServiceConnection

class Outpost(BaseModel):
    """
    Outpost Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    type: OutpostTypeEnum = Field(...)
    providers: conlist(StrictInt) = Field(...)
    providers_obj: conlist(Provider) = Field(...)
    service_connection: Optional[StrictStr] = Field(None, description="Select Service-Connection authentik should use to manage this outpost. Leave empty if authentik should not handle the deployment.")
    service_connection_obj: ServiceConnection = Field(...)
    token_identifier: StrictStr = Field(..., description="Get Token identifier")
    config: Dict[str, Any] = Field(...)
    managed: Optional[StrictStr] = Field(None, description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    __properties = ["pk", "name", "type", "providers", "providers_obj", "service_connection", "service_connection_obj", "token_identifier", "config", "managed"]

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
    def from_json(cls, json_str: str) -> Outpost:
        """Create an instance of Outpost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "providers_obj",
                            "service_connection_obj",
                            "token_identifier",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in providers_obj (list)
        _items = []
        if self.providers_obj:
            for _item in self.providers_obj:
                if _item:
                    _items.append(_item.to_dict())
            _dict['providers_obj'] = _items
        # override the default output from pydantic by calling `to_dict()` of service_connection_obj
        if self.service_connection_obj:
            _dict['service_connection_obj'] = self.service_connection_obj.to_dict()
        # set to None if service_connection (nullable) is None
        # and __fields_set__ contains the field
        if self.service_connection is None and "service_connection" in self.__fields_set__:
            _dict['service_connection'] = None

        # set to None if managed (nullable) is None
        # and __fields_set__ contains the field
        if self.managed is None and "managed" in self.__fields_set__:
            _dict['managed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Outpost:
        """Create an instance of Outpost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Outpost.parse_obj(obj)

        _obj = Outpost.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "providers": obj.get("providers"),
            "providers_obj": [Provider.from_dict(_item) for _item in obj.get("providers_obj")] if obj.get("providers_obj") is not None else None,
            "service_connection": obj.get("service_connection"),
            "service_connection_obj": ServiceConnection.from_dict(obj.get("service_connection_obj")) if obj.get("service_connection_obj") is not None else None,
            "token_identifier": obj.get("token_identifier"),
            "config": obj.get("config"),
            "managed": obj.get("managed")
        })
        return _obj


