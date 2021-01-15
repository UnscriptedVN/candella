#
# AppStorage.rpy
# Candella Multiuser
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -10

init python:
    class AppStorage():
        """A class for app storage in Candella applications.
        
        This class allows Candella apps to read/write data for their app. Typically, this can be used for settings
            or small persistent data.
        """
        
        _data_store = {}
        
        def __init__(self, app, user=persistent.playername):
            """Initialize an AppStorage unit.
            
            Arguments:
                app (CAApplication): The application to give the data store to.
                user (str): A specified username. Defaults to the current user.
            """
            self._current_user = user
            
            if not isinstance(app, CAApplication):
                raise Exception
            if "file_system" not in app.permissions:
                raise Exception
            
            self._bundle_id = app.id
            
            try:
                self._data_store = CSUserData.get_current_user_data(self._bundle_id)
            except:
                self._data_store = {}
        
        def read(self, field):
            """Returns the value of a field in the storage, or None if the value doesn't exist.
            
            Use `AppStorage.read_not_none` if the value in question cannot be None.
            """
            return self._data_store.get(field, None)
        
        def read_not_none(self, field):
            """Returns the value of a field in the storage.
            
            Raises:
                If the value does not exist, KeyError will be raised.
            """
            if field not in self._data_store:
                raise KeyError
            if self._data_store[field] is None:
                raise KeyError
            return self._data_store[field]
                
        def write(self):
            """Write the app data to the current user's file."""
            try:
                CAUserData.write_data_to_current_user(self._bundle_id, self._data_store)
            except Exception as error:
                print("ERR: Data could not be written. Reason: %s" % (error))