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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from authentik.models.challenge_choices import ChallengeChoices
from authentik.models.contextual_flow_info import ContextualFlowInfo
from authentik.models.error_detail import ErrorDetail

class AuthenticatorSMSChallenge(BaseModel):
    """
    SMS Setup challenge
    """
    type: ChallengeChoices = Field(...)
    flow_info: Optional[ContextualFlowInfo] = None
    component: Optional[StrictStr] = 'ak-stage-authenticator-sms'
    response_errors: Optional[Dict[str, conlist(ErrorDetail)]] = None
    pending_user: StrictStr = Field(...)
    pending_user_avatar: StrictStr = Field(...)
    phone_number_required: Optional[StrictBool] = True
    __properties = ["type", "flow_info", "component", "response_errors", "pending_user", "pending_user_avatar", "phone_number_required"]

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
    def from_json(cls, json_str: str) -> AuthenticatorSMSChallenge:
        """Create an instance of AuthenticatorSMSChallenge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_info
        if self.flow_info:
            _dict['flow_info'] = self.flow_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in response_errors (dict of array)
        _field_dict_of_array = {}
        if self.response_errors:
            for _key in self.response_errors:
                if self.response_errors[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.response_errors[_key]
                    ]
            _dict['response_errors'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticatorSMSChallenge:
        """Create an instance of AuthenticatorSMSChallenge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatorSMSChallenge.parse_obj(obj)

        _obj = AuthenticatorSMSChallenge.parse_obj({
            "type": obj.get("type"),
            "flow_info": ContextualFlowInfo.from_dict(obj.get("flow_info")) if obj.get("flow_info") is not None else None,
            "component": obj.get("component") if obj.get("component") is not None else 'ak-stage-authenticator-sms',
            "response_errors": dict(
                (_k,
                        [ErrorDetail.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("response_errors").items()
            ),
            "pending_user": obj.get("pending_user"),
            "pending_user_avatar": obj.get("pending_user_avatar"),
            "phone_number_required": obj.get("phone_number_required") if obj.get("phone_number_required") is not None else True
        })
        return _obj


