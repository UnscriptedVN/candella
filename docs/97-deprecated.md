# Deprecations

Candella includes a small module that facilitates deprecating functions or restricting function to specific OS versions.

## `available` {label:new}
Restrict usage of a function to specific OS versions. This can be used to determine if a method or function should be marked as deprecated, or if a function is only available on a specific minimum OS version. This decorator is inspired by the `@available` property wrapper in Swift.

```py
from store.CADeprecated import available

# To mark a function as available for all OS versions.
@available("*", introduced="bahama")
def new_test_function():
    return True

# To mark a function as available to a minimum version.
@available("bahama", introduced="bahama")
def requires_bahama():
    return new_test_function() and False

# To mark a function as deprecated in a given version.
@available("*", deprecated="bahama", message="Please use new_test_function instead.")
def is_truthy():
    return True
```

### Arguments
- minimum_codename (str): The minimum OS version that this function supports. To support all, use '*'.
- introduced (str): The OS version that this function was introduced. Defaults to apple-cinnamon.
- deprecated (str): The OS version that this function was deprecated. Defaults to None.
- message (str): A message used to mark why something is deprecated or introduced. Defaults to None.

## `@deprecated` {label:deprecated}

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