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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class SAMLPropertyMapping(BaseModel):
    """
    SAMLPropertyMapping Serializer
    """
    pk: StrictStr = Field(...)
    managed: Optional[StrictStr] = Field(None, description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    name: StrictStr = Field(...)
    expression: StrictStr = Field(...)
    component: StrictStr = Field(..., description="Get object's component so that we know how to edit the object")
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    saml_name: StrictStr = Field(...)
    friendly_name: Optional[StrictStr] = None
    __properties = ["pk", "managed", "name", "expression", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "saml_name", "friendly_name"]

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
    def from_json(cls, json_str: str) -> SAMLPropertyMapping:
        """Create an instance of SAMLPropertyMapping from a JSON string"""
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
        # set to None if managed (nullable) is None
        # and __fields_set__ contains the field
        if self.managed is None and "managed" in self.__fields_set__:
            _dict['managed'] = None

        # set to None if friendly_name (nullable) is None
        # and __fields_set__ contains the field
        if self.friendly_name is None and "friendly_name" in self.__fields_set__:
            _dict['friendly_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SAMLPropertyMapping:
        """Create an instance of SAMLPropertyMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SAMLPropertyMapping.parse_obj(obj)

        _obj = SAMLPropertyMapping.parse_obj({
            "pk": obj.get("pk"),
            "managed": obj.get("managed"),
            "name": obj.get("name"),
            "expression": obj.get("expression"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "saml_name": obj.get("saml_name"),
            "friendly_name": obj.get("friendly_name")
        })
        return _obj


