from collections.abc import Sequence
from typing import TYPE_CHECKING, Annotated, Any, Optional

from ravyn import ChildRavyn, Ravyn
from ravyn.core.interceptors.types import Interceptor
from ravyn.permissions.types import Permission
from ravyn.pluggables import Extension
from ravyn.routing.router import Include
from ravyn.types import Dependencies, ExceptionHandlerMap, Middleware
from typing_extensions import Doc

if TYPE_CHECKING:
    from ravyn.types import SettingsType


class SimpleJWTExtension(Extension):
    """
    The pluggable version of Ravyn Simple JWT.

    This Pluggable can and should be used if you want to add
    the package independently as a ChilRavyn.

    **Example**

    ```python
    from ravyn import Ravyn, Pluggable
    from ravyn_simple_jwt.extension import SimpleJWTExtension


    app = Ravyn(
        extensions={
            "simple-jwt": Pluggable(SimpleJWTExtension, path="/auth"),
        },
    )
    ```
    """

    def __init__(self, app: Optional["Ravyn"] = None, **kwargs: Any):
        super().__init__(app, **kwargs)
        self.app = app
        self.kwargs = kwargs

    def extend(
        self,
        path: Annotated[
            str | None,
            Doc(
                """
                Relative path of the Plugable.
                The path can contain parameters in a dictionary like format
                and if the path is not provided, it will default to `/`.

                **Example**

                ```python
                Pluugable(SimpleJWTExtension, path="/{age: int}"))
                ```
                """
            ),
        ] = "/simple-jwt",
        name: Annotated[
            str | None,
            Doc(
                """
                The name for the Gateway. The name can be reversed by `url_path_for()`.
                """
            ),
        ] = None,
        settings_module: Annotated[
            Optional["SettingsType"],
            Doc(
                """
                Alternative settings parameter. This parameter is an alternative to
                `RAVYN_SETTINGS_MODULE` way of loading your settings into an Ravyn application.

                When the `settings_module` is provided, it will make sure it takes priority over
                any other settings provided for the instance.

                Read more about the [settings module](https://ravyn.dev/application/settings/)
                and how you can leverage it in your application.

                !!! Tip
                    The settings module can be very useful if you want to have, for example, a
                    [ChildRavyn](https://ravyn.dev/routing/router/?h=childe#child-ravyn-application) that needs completely different settings
                    from the main app.

                    Example: A `ChildRavyn` that takes care of the authentication into a cloud
                    provider such as AWS and handles the `boto3` module.
                """
            ),
        ] = None,
        middleware: Annotated[
            Sequence["Middleware"] | None,
            Doc(
                """
                A list of middleware to run for every request. The middlewares of a Gateway will be checked from top-down or [Starlette Middleware](https://www.starlette.io/middleware/) as they are both converted internally. Read more about [Python Protocols](https://peps.python.org/pep-0544/).
                """
            ),
        ] = None,
        dependencies: Annotated[
            Optional["Dependencies"],
            Doc(
                """
                A dictionary of string and [Inject](https://ravyn.dev/dependencies/) instances enable application level dependency injection.
                """
            ),
        ] = None,
        exception_handlers: Annotated[
            Optional["ExceptionHandlerMap"],
            Doc(
                """
                A dictionary of [exception types](https://ravyn.dev/exceptions/) (or custom exceptions) and the handler functions on an application top level. Exception handler callables should be of the form of `handler(request, exc) -> response` and may be be either standard functions, or async functions.
                """
            ),
        ] = None,
        interceptors: Annotated[
            list["Interceptor"] | None,
            Doc(
                """
                A list of [interceptors](https://ravyn.dev/interceptors/) to serve the application incoming requests (HTTP and Websockets).
                """
            ),
        ] = None,
        permissions: Annotated[
            list["Permission"] | None,
            Doc(
                """
                A list of [permissions](https://ravyn.dev/permissions/) to serve the application incoming requests (HTTP and Websockets).
                """
            ),
        ] = None,
        include_in_schema: Annotated[
            bool | None,
            Doc(
                """
                Boolean flag indicating if it should be added to the OpenAPI docs.
                """
            ),
        ] = True,
        enable_openapi: Annotated[
            bool | None,
            Doc(
                """
                Boolean flag indicating if the OpenAPI documentation should
                be generated or not.

                When `False`, no OpenAPI documentation is accessible.

                !!! Tip
                    Disable this option if you run in production and no one should access the
                    documentation unless behind an authentication.
                ```
                """
            ),
        ] = True,
    ) -> None:
        """
        The extend() default from the Pluggable interface allowing to pass extra parameters
        to the initialisation.

        **Example**

        ```python
        from ravyn import Ravyn, Pluggable
        from ravyn_simple_jwt.extension import SimpleJWTExtension


        app = Ravyn(
            extensions={
                "simple-jwt": Pluggable(
                    SimpleJWTExtension,
                    path="/auth",
                    settings_module=...,
                    middleware=...,
                    permissions=...,
                    interceptors=...,
                ),
            },
        )
        ```
        """
        simple_jwt = ChildRavyn(
            routes=[
                Include(namespace="ravyn_simple_jwt.urls"),
            ],
            middleware=middleware,
            dependencies=dependencies,
            exception_handlers=exception_handlers,
            interceptors=interceptors,
            permissions=permissions,
            include_in_schema=include_in_schema,
            enable_openapi=enable_openapi,
            settings_module=settings_module,
        )
        self.app.add_child_ravyn(
            path=path,
            child=simple_jwt,
            name=name,
            include_in_schema=include_in_schema,
        )
