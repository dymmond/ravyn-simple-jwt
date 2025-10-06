import pytest
from ravyn.conf import settings
from ravyn.contrib.auth.edgy.base_user import AbstractUser

database, models = settings.edgy_registry
pytestmark = pytest.mark.anyio


class User(AbstractUser):
    """
    Inherits from the abstract user and adds the registry
    from ravyn settings.
    """

    class Meta:
        registry = models
