from typing import Optional

import jwt
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal
from cerbos.sdk.model import Resource
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from conf.settings import Settings


def decode_token(token: str):
    print(token)
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms="HS256")
        return payload
    except jwt.ExpiredSignatureError as err:
        print("expired", err)
        raise HTTPException(status_code=401, detail="Invalid Token")
    except jwt.InvalidTokenError as err:
        print("invalid", err)
        raise HTTPException(status_code=401, detail="Invalid token")


def get_resource_id_from_request(request: Request):
    return request.path_params.get("resource_id")


class PermissionValidator(HTTPBearer):
    def __init__(
        self, action: str, resource_kind: str, get_resource_id, auto_error: bool = True
    ):
        super().__init__(auto_error=auto_error)
        self.action = action
        self.resource_kind = resource_kind
        self.get_resource_id = get_resource_id
        self.cerbos_client = CerbosClient(host="http://localhost:3592")

    async def __call__(self, request: Request) -> Optional[dict]:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Authentication required"
            )

        payload = decode_token(credentials.credentials)

        # Get the resource ID from the request
        resource_id = self.get_resource_id(request)

        principal = Principal(
            id=payload.get("sub"),
            roles=set(payload.get("roles", [])),
            attr=payload.get("attr"),
        )

        resource = Resource(
            id=resource_id,
            kind=self.resource_kind,
            attr={
                "region": "eu-east-1",
                "ownerId": payload.get("sub")
            },
        )

        if not self.cerbos_client.is_allowed(self.action, principal, resource):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to perform this action!"
            )

        return payload