#
# CAObservable.rpy
# AppKit (Candella)
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -50

init python:
    import logging
    
    class CAObservable():
        """A class that can be observed by methods."""
        _observers = []
        
        def __init__(self):
            self._observers = []
        
        def register_event(self, callable):
            """Register an event to listen to this observable class.
            
            Arguments:
                callable (callable): The method that will listen for changes.
            """
            self._observers.append(callable)
            clog.debug("Registered new event to class %s.", self.__class__.__name__)
            return callable
        
        def emit_signal(self, *args, **kwargs):
            """Emit a signal to all known observers of this class."""
            clog.debug("Emitting signal %s to observers of %s.", args, self.__class__.__name__)
            for emit in self._observers:
                emit(*args, **kwargs)