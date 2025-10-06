import pytest
from ravyn import Include, Ravyn
from ravyn.conf import settings
from ravyn.testclient import RavynTestClient

database, models = settings.edgy_registry


def create_app():
    from edgy import Instance, monkay

    # ensure the settings are loaded
    monkay.evaluate_settings(
        ignore_preload_import_errors=False,
        onetime=False,
    )
    app = Ravyn(routes=[Include(path="/simple-jwt", namespace="ravyn_simple_jwt.urls")])
    monkay.set_instance(Instance(registry=app.settings.registry, app=app))
    return app


def get_client():
    return RavynTestClient(create_app())


@pytest.fixture(scope="module")
def anyio_backend():
    return ("asyncio", {"debug": False})


@pytest.fixture
def app():
    return create_app()


@pytest.fixture(autouse=True, scope="function")
async def create_test_database():
    async with models.database:
        await models.create_all()
        yield
        if not models.database.drop:
            await models.drop_all()


@pytest.fixture(autouse=True, scope="function")
async def rollback_transactions():
    async with models.database:
        yield
