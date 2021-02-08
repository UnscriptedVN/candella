# Observable

Observable is a Candella framework designed to add observability to classes, similar to what's offered in languages like Java.

## What uses Observable?

Candella uses Observable in a few places:

- In **AppKit**, all apps inherit the `CAObservable` class and can emit signals to observers.
- In **ServiceKit**, core services inherit `CAObservable` and emit signals to observers.
- In **Caberto Shell**, the service listens for signal emissions and acts as an observer with a callback method.

## Logic

To use Observable, you need to have two things: an observable item that subclasses from `CAObservable`, and a callback method that listens for signals when they're emitted.

Let's say that we're making some sort of logger that listens for when apps are opened. We can do the following to accomplish this:

```py
def callback(*args, **kwargs):
    if "application_launched" not in args:
        return
    appname = kwargs["name"] if "name" in kwargs else "Application"
    print(appname + " was launched!")

class App(CAObservable):
    def __init__(self):
        CAObservable.__init__(self)
        self.register_event(callback)

    def open(self):
        self.emit_signal("application_launched", self.__class__.__name__)
```

When the `open` method on the `App` class is called, the callback function will receive that update and trigger accordingly.

## `CAObservable`
A class that can be observed by methods.

### `register_event(callable)`
Register an event to listen to this observable class.

**Arguments**

- callable (callable): The method that will listen for changes.

### `emit_signal(*args, **kwargs)`

Emit a signal to all known observers of this class. The signal's identifier should be passed in `args` and any additional data should be passed as a keyword argument in `kwargs`.