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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint
from authentik.models.ldapapi_access_mode import LDAPAPIAccessMode

class LDAPOutpostConfig(BaseModel):
    """
    LDAPProvider Serializer
    """
    pk: StrictInt = Field(...)
    name: StrictStr = Field(...)
    base_dn: Optional[StrictStr] = Field(None, description="DN under which objects are accessible.")
    bind_flow_slug: StrictStr = Field(...)
    application_slug: StrictStr = Field(..., description="Prioritise backchannel slug over direct application slug")
    search_group: Optional[StrictStr] = Field(None, description="Users in this group can do search queries. If not set, every user can execute search queries.")
    certificate: Optional[StrictStr] = None
    tls_server_name: Optional[StrictStr] = None
    uid_start_number: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = Field(None, description="The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren't too low for POSIX users. Default is 2000 to ensure that we don't collide with local users uidNumber")
    gid_start_number: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = Field(None, description="The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren't too low for POSIX groups. Default is 4000 to ensure that we don't collide with local groups or users primary groups gidNumber")
    search_mode: Optional[LDAPAPIAccessMode] = None
    bind_mode: Optional[LDAPAPIAccessMode] = None
    mfa_support: Optional[StrictBool] = Field(None, description="When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon.")
    __properties = ["pk", "name", "base_dn", "bind_flow_slug", "application_slug", "search_group", "certificate", "tls_server_name", "uid_start_number", "gid_start_number", "search_mode", "bind_mode", "mfa_support"]

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
    def from_json(cls, json_str: str) -> LDAPOutpostConfig:
        """Create an instance of LDAPOutpostConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "application_slug",
                          },
                          exclude_none=True)
        # set to None if search_group (nullable) is None
        # and __fields_set__ contains the field
        if self.search_group is None and "search_group" in self.__fields_set__:
            _dict['search_group'] = None

        # set to None if certificate (nullable) is None
        # and __fields_set__ contains the field
        if self.certificate is None and "certificate" in self.__fields_set__:
            _dict['certificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LDAPOutpostConfig:
        """Create an instance of LDAPOutpostConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LDAPOutpostConfig.parse_obj(obj)

        _obj = LDAPOutpostConfig.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "base_dn": obj.get("base_dn"),
            "bind_flow_slug": obj.get("bind_flow_slug"),
            "application_slug": obj.get("application_slug"),
            "search_group": obj.get("search_group"),
            "certificate": obj.get("certificate"),
            "tls_server_name": obj.get("tls_server_name"),
            "uid_start_number": obj.get("uid_start_number"),
            "gid_start_number": obj.get("gid_start_number"),
            "search_mode": obj.get("search_mode"),
            "bind_mode": obj.get("bind_mode"),
            "mfa_support": obj.get("mfa_support")
        })
        return _obj


