from ravyn import Include, Ravyn

app = Ravyn(
    routes=[
        Include(path="/auth", namespace="ravyn_simple_jwt.urls"),
    ]
)
