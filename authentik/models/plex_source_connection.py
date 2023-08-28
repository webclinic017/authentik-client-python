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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from authentik.models.source import Source

class PlexSourceConnection(BaseModel):
    """
    Plex Source connection Serializer
    """
    pk: StrictInt = Field(...)
    user: StrictInt = Field(...)
    source: Source = Field(...)
    identifier: StrictStr = Field(...)
    plex_token: StrictStr = Field(...)
    __properties = ["pk", "user", "source", "identifier", "plex_token"]

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
    def from_json(cls, json_str: str) -> PlexSourceConnection:
        """Create an instance of PlexSourceConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "user",
                            "source",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlexSourceConnection:
        """Create an instance of PlexSourceConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlexSourceConnection.parse_obj(obj)

        _obj = PlexSourceConnection.parse_obj({
            "pk": obj.get("pk"),
            "user": obj.get("user"),
            "source": Source.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "identifier": obj.get("identifier"),
            "plex_token": obj.get("plex_token")
        })
        return _obj


