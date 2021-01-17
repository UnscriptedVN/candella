#
# CAUser.rpy
# Multiuser
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -10

init python:
    class CAUser():
        """A data class that represents a user."""
        
        username = "user"
        display_name = "Foo Bar"
        
        # TODO: Add password protections?
        
        def __init__(self, username, display_name):
            self.username = username
            self.display_name = display_name
            
        def __eq__(self, other):
            return isinstance(other, CAUser) and self.username == other.username
            
        def __ne__(self, other):
            return not self.__eq__(other)
            
        def __repr__(self):
            return "CAUser(%s<%s>)" % (self.display_name, self.username)
            
        def __str__(self):
            return "CAUser(%s<%s>)" % (self.display_name, self.username)