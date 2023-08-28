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
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class RadiusProviderRequest(BaseModel):
    """
    RadiusProvider Serializer
    """
    name: constr(strict=True, min_length=1) = Field(...)
    authentication_flow: Optional[StrictStr] = Field(None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: StrictStr = Field(..., description="Flow used when authorizing this provider.")
    property_mappings: Optional[conlist(StrictStr)] = None
    client_networks: Optional[constr(strict=True, min_length=1)] = Field(None, description="List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped.")
    shared_secret: Optional[constr(strict=True, min_length=1)] = Field(None, description="Shared secret between clients and server to hash packets.")
    __properties = ["name", "authentication_flow", "authorization_flow", "property_mappings", "client_networks", "shared_secret"]

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
    def from_json(cls, json_str: str) -> RadiusProviderRequest:
        """Create an instance of RadiusProviderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if authentication_flow (nullable) is None
        # and __fields_set__ contains the field
        if self.authentication_flow is None and "authentication_flow" in self.__fields_set__:
            _dict['authentication_flow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RadiusProviderRequest:
        """Create an instance of RadiusProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RadiusProviderRequest.parse_obj(obj)

        _obj = RadiusProviderRequest.parse_obj({
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "client_networks": obj.get("client_networks"),
            "shared_secret": obj.get("shared_secret")
        })
        return _obj


