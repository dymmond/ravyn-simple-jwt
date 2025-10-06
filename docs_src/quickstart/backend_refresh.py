from datetime import datetime

from jwt.exceptions import PyJWTError
from ravyn.conf import settings
from ravyn.exceptions import AuthenticationError, NotAuthorized

from ravyn_simple_jwt.backends import BaseRefreshAuthentication
from ravyn_simple_jwt.schemas import AccessToken, RefreshToken
from ravyn_simple_jwt.token import Token


class RefreshAuthentication(BaseRefreshAuthentication):
    """
    Refreshes the access token given a refresh token of a given user.

    This object does not perform any DB action, instead, uses the existing refresh
    token to generate a new access.
    """

    token: RefreshToken

    async def refresh(self) -> AccessToken:
        token = self.token.refresh_token

        try:
            token = Token.decode(
                token=token,
                key=settings.simple_jwt.signing_key,
                algorithms=[settings.simple_jwt.algorithm],
            )
        except PyJWTError as e:
            raise AuthenticationError(str(e)) from e

        if token.token_type != settings.simple_jwt.refresh_token_name:
            raise NotAuthorized(detail="Only refresh tokens are allowed.")

        # Apply the maximum living time
        expiry_date = datetime.now() + settings.simple_jwt.access_token_lifetime

        # New token object
        new_token = Token(sub=token.sub, exp=expiry_date)

        # Encode the token
        claims_extra = {"token_type": settings.simple_jwt.access_token_name}
        access_token = new_token.encode(
            key=settings.simple_jwt.signing_key,
            algorithm=settings.simple_jwt.algorithm,
            claims_extra=claims_extra,
        )

        return AccessToken(access_token=access_token)
