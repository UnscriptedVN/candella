#
# AppStorage.rpy
# Candella Multiuser
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -10

init python:
    from store.CADeprecated import deprecated
    import logging

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
                self._data_store = CAUserData.get_current_user_data(self._bundle_id)
            except:
                self._data_store = {}


        def get_entry(self, field, raise_falsy=False):
            """Returns the entry in a specified field.

            Arguments:
                field (str): The field to retrieve a value for.
                raise_falsy (bool): Whether to raise an Exception when there is no value associated with the field.
                    Defaults to False.
            """
            entry = self._data_store.get(field, None)
            if not entry and raise_falsy:
                raise KeyError
            return entry


        def set_entry(self, field, result):
            """Sets the field to the result in the current storage."""
            self._data_store[field] = result


        def commit(self):
            """Write the app data to the current user's file."""
            try:
                CAUserData.write_data_to_current_user(self._bundle_id, self._data_store)
            except Exception as error:
                logging.error("Data could not be written. Reason: %s", error)
