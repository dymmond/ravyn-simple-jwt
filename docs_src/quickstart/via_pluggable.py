from ravyn import Pluggable, Ravyn

from ravyn_simple_jwt.extension import SimpleJWTExtension

app = Ravyn(
    extensions={
        "simple-jwt": Pluggable(SimpleJWTExtension, path="/auth"),
    },
)
