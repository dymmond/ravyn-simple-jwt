import os

from myapp.backends import BackendAuthentication, RefreshAuthentication
from ravyn import RavynSettings

from ravyn_simple_jwt.config import SimpleJWT

DATABASE_URL = os.environ.get("DATABASE_URI", "sqlite:///db.sqlite")


class AppSettings(RavynSettings):
    """
    The settings object for the application.
    """

    @property
    def simple_jwt(self) -> SimpleJWT:
        return SimpleJWT(
            signing_key=self.secret_key,
            backend_authentication=BackendAuthentication,
            backend_refresh=RefreshAuthentication,
        )
