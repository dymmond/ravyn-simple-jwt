from ravyn.conf import settings
from ravyn.contrib.auth.edgy.base_user import AbstractUser

# These configurations are loaded
# from the application settings
# check the `settings.py`.
database, models = settings.db_connection


class User(AbstractUser):
    """
    Model using the Esmerald contrib for
    Edgy and providing useful functionality for
    any application.
    """

    class Meta:
        registry = models
