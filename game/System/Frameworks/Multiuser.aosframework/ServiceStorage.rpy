#
# ServiceStorage.rpy
# Candella Multiuser
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init python:
    from store.CADeprecated import deprecated
    import logging

    class ServiceStorage():
        """A class for app storage in Candella services."""

        _data_store = {}


        def __init__(self, service, user=persistent.playername):
            """Initialize a ServiceStorage unit.

            Arguments:
                service (ASCoreServiceRepresentative): The core service to give the data store to.
                user (str): A specified username. Defaults to the current user.
            """
            self._current_user = user

            if not isinstance(service, ASCoreServiceRepresentative):
                raise Exception

            self._bundle_id = service.bundleId

            try:
                self._data_store = CAUserData.get_current_user_data(self._bundle_id)
            except Exception as error:
                self._data_store = {}


        def __str__(self):
            return str(self._data_store)


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


        @deprecated('21.02', renamed="get_entry")
        def read(self, field):
            """Returns the value of a field in the storage, or None if the value doesn't exist.

            Use `AppStorage.read_not_none` if the value in question cannot be None.
            """
            return self.get_entry(field)


        @deprecated('21.02', reason="Use get_entry with the argument 'raise_falsy' set to True.")
        def read_not_none(self, field):
            """Returns the value of a field in the storage.

            Raises:
                If the value does not exist, KeyError will be raised.
            """
            return self.get_entry(field, raise_falsy=True)


        def set_entry(self, field, result):
            """Sets the field to the result in the current storage."""
            self._data_store[field] = result


        @deprecated('21.02', renamed="set_entry")
        def write_field(self, field, result):
            """Sets the field to the result in the current storage."""
            self.set_entry(field, result)


        def commit(self):
            """Write the app data to the current user's file."""
            try:
                CAUserData.write_data_to_current_user(self._bundle_id, self._data_store)
            except Exception as error:
                logging.error(
                    "Data could not be written. Reason: %s (%s)",
                    error,
                    error.__class__.__name__
                )

        @deprecated('21.02', renamed="commit")
        def write(self):
            """Write the app data to the current user's file."""
            self.commit()
