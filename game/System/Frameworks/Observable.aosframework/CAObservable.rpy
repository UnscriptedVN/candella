#
# CAObservable.rpy
# AppKit (Candella)
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -49

init python:
    import logging
    from store.CADeprecated import available

    class CAObservable():
        """A class that can be observed by methods."""
        _observers = []

        def __init__(self):
            self._observers = []

        @available('*', introduced="apple-cinnamon")
        def register_event(self, callable):
            """Register an event to listen to this observable class.

            Arguments:
                callable (callable): The method that will listen for changes.
            """
            self._observers.append(callable)
            clog.info("Registered new event to class %s.", self.__class__.__name__)
            return callable

        @available('*', introduced="apple-cinnamon")
        def emit_signal(self, *args, **kwargs):
            """Emit a signal to all known observers of this class."""
            clog.debug("Emitting signal '%s' to observers of %s.", args[0], self.__class__.__name__)
            for emit in self._observers:
                emit(*args, **kwargs)
