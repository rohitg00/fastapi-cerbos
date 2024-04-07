import json
import os
import sys
import uuid
from datetime import datetime
from datetime import timedelta

import jwt
from dotenv import load_dotenv

load_dotenv()


def create_jwt_token(principal, roles, attr, secret_key, algorithm="HS256"):
    # Standard claims
    payload = {
        "iss": "Cerbos",  # Issuer of the token
        "sub": principal,  # Subject of the token (principal)
        "exp": datetime.utcnow() + timedelta(days=1),  # Expiration time
        "iat": datetime.utcnow(),  # Issued at time
        # Custom claims
        "roles": roles,
        "id": str(uuid.uuid4()),
        "attr": attr,
    }

    return jwt.encode(payload, secret_key, algorithm=algorithm)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python script.py 'test@test.com' '[\"user\"]' '{\"region\": \"eu-east-1\"}'"  # noqa
        )
        sys.exit(1)

    principal_input = sys.argv[1]
    roles_input = sys.argv[2]
    attr_input = sys.argv[3]

    try:
        roles = json.loads(roles_input)
        attr = json.loads(attr_input)
    except json.JSONDecodeError:
        print("Invalid JSON format for roles or attr")
        sys.exit(1)

    secret_key = os.getenv("SECRET_KEY")  # Load secret key from environment variables

    token = create_jwt_token(principal_input, roles, attr, secret_key)
    print(f"JWT Token: {token}")
