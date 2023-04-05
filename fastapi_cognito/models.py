from typing import Union, List, Set, Optional, Tuple

from pydantic import BaseModel, HttpUrl, Field


class UserpoolModel(BaseModel):
    region: str
    userpool_id: str
    app_client_id: Union[str, List[str], Set[str], Tuple[str]]


class CognitoToken(BaseModel):
    origin_jti: str
    cognito_id: str = Field(alias="sub")
    event_id: Optional[str]
    token_use: str
    scope: str
    auth_time: int
    iss: HttpUrl
    exp: int
    iat: int
    jti: str
    client_id: str
    username: str


class CBECognitoToken(BaseModel):
    cognito_id: str = Field(alias="sub")
    event_id: Optional[str]
    token_use: str
    auth_time: int
    exp: int
    iat: int
    groups: List[str] = Field(alias="cognito:groups")
    username: str = Field(alias="cognito:username")
    debtor_number: str = Field(alias='custom:debtor_number')
    seller_id: str = Field(alias='custom:seller_id')
    relation_id: str = Field(alias='custom:relation_id')
    domain: str = Field(alias='custom:domain')
