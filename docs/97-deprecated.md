# Deprecations

Candella includes a small module that facilitates deprecating functions. To mark a function as deprecated, import the function and decorate the function you want to deprecate:

```py
from store.CADeprecated import deprecated

@deprecated('21.02')
def deprecated_func():
    pass

```

When the function is called, a warning message will appear in the console and the Candella log file indicating that the function was deprecated, as well as the reason for the deprecation, if one was specified.

!!! important
    The `deprecated` function has been tested on functions and class methods, but hasn't been tested or designed for variables, class fields, or classes themselves. Use with caution.

## `deprecated` arguments

- `version` (str): The version in which the function will be deprecated.
- `renamed` (str): (Optional) What the function has been renamed to, if the function was renamed.
- `reason` (str): (Optional) The reason why the function was deprecated.