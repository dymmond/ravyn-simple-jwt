# Pluggable

The Pluugable object is the one of the ways of importing the Ravyn Simple JWT into your Ravyn
application via *installation* of the package.

```python
{!> ../docs_src/quickstart/via_pluggable.py !}
```

Ravyn [official documentation abuot Pluggables](https://ravyn.dev/pluggables/) goes into
great detail about how to use it and when to use it.

In other words, what Ravyn Simple JWT pluggable does is to simple install a [ChildRavyn](https://ravyn.dev/routing/router/#child-ravyn-application)
module inside the Ravyn application using the pluggable itself.

Since Ravyn is modular, it could be inside the main Ravyn application or inside any nested
Ravyn or ChildRavyn objects.

It is your choice.

## API Reference

You can check all the available parameters to use with this simple configuration in the
[Pluggable API Reference](./references/pluggable.md).
