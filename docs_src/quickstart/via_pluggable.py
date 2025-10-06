from ravyn import Pluggable, Ravyn

from ravyn_simple_jwt.extension import SimpleJWTExtension

app = Ravyn(
    pluggables={
        "simple-jwt": Pluggable(SimpleJWTExtension, path="/auth"),
    },
)
