from typing import Annotated

from ravyn.security.jwt.token import Token as RavynToken
from typing_extensions import Doc


class Token(RavynToken):
    """
    Token implementation with an extra field
    `token_type`. This attribute will allow
    the distintion of the type of token being generated.

    This token is an extension of the `ravyn.security.jwt.Token` object
    and adds some extras that are used by the default Refresh backend provided
    by the package.

    !!! Note
        You are not entitled to use this object at all in your backends but if you
        are to use the examples given and the defaults without wasting too much time
        the package examples use this object to classiify the `token_type` in the claims.
    """

    token_type: Annotated[
        str | None,
        Doc(
            """
            A string value classifying the type of token being generated and used
            for the claims.

            It can be something like `access_token` or `access` or
            `refresh_token` or `refresh` or any other string value
            that can help you distinguish the token being generated in the
            claims when `decode()` and `encode()` are called.
            """
        ),
    ] = None
