#
# UserData.rpy
# Candella Multiuser
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -10

init python:
    import os
    import json
    
    class CAUserDataNotFoundError(Exception):
        """User data not found."""
    
    class CAUserDataPermissionError(Exception):
        """An exception used when the app doesn't have permission to access user data."""
    
    class CAUserData():
        """A class dedicated for user data."""
        
        username = "user"
        data_path = config.savedir + "/.causerland"
        
        _data = {}
        
        def __init__(self, user):
            self.username = user.lower().replace(" ", "")
            data_file = self.data_path + "/" + user
            
            if not os.path.isfile(data_file):
                CAUserData._create_user_file(user)
                self._data = { "name": user, "prettyName": user }
            else:
                with open(data_file, 'r') as data_object:
                    self._data = json.load(data_object)
        
        @staticmethod
        def _create_user_file(username, pretty_name=None):
            """Create a user data file for a user.
            
            Arguments:
                username (str): The username to create a data file for. If the username contains spaces or capital
                    letters, the username will automatically be lowercased and spaces will be removed.
            """
            ca_username = username.lower().replace(" ", "")
            data = { "name": username, "prettyName": pretty_name if pretty_name else username }
            if not os.path.isdir(config.savedir + "/.causerland/"):
                os.mkdir("%s/.causerland" % (config.savedir))
            with open("%s/.causerland/%s" % (config.savedir, username), 'wb+') as file:
                json.dump(data, file)
                
        @staticmethod
        def __file_permissible(bundle_id):
            """Returns whether the app with a given bundle ID has permission to write to user files."""
            _perms = persistent.AS_PERMISSIONS
            return bundle_id in _perms and "REQ_FULL_DISK" in _perms[bundle_id] and _perms[bundle_id]["REQ_FULL_DISK"]
            
        @staticmethod
        def get_current_user_data(bundle_id):
            """Returns the application data for the current user.
            
            Arguments:
                bundle_id (str): The app's bundle ID.
            
            Returns:
                app_data (dict): The user data for the specified app as a dictionary. If no data was found for the app,
                    an empty dictionary will be returned.
            
            Raises:
                If the app doesn't have permissions to open the data, CAUserDataPermissionError is raised.
                    If the user file doesn't exist, FileNotFoundError is raised. Otherwise, any other
                    exceptions from file opening and parsing may be thrown.
            """
            app_data = {}
            if not CAUserData.__file_permissible(bundle_id):
                raise CAUserDataPermissionError
            
            if not os.path.isfile(config.savedir + "/.causerland/" + persistent.playername):
                raise CAUserDataNotFoundError(config.savedir + "/.causerland/" + persistent.playername)
            
            with open(config.savedir + "/.causerland/" + persistent.playername, 'rb') as file:
                data = json.load(file)
            
            if bundle_id in data:
                app_data = data[bundle_id]
            return app_data
            
        @staticmethod
        def write_data_to_current_user(bundle_id, data={}):
            """Writes the specified app data to the current user's file.
            
            Arguments:
                bundle_id (str): The app's bundle ID
                data (dict): The data to write to the file for that bundle ID.
            
            Raises:
                If the app doesn't have permissions to write the data, CAUserDataPermissionError is raised.
                    If the user file doesn't exist, FileNotFoundError is raised. Otherwise, any other
                    exceptions from file opening and writing may be thrown.
            """
            if not CAUserData.__file_permissible(bundle_id):
                raise CAUserDataPermissionError
            
            if not os.path.isfile(config.savedir + "/.causerland/" + persistent.playername):
                raise CAUserDataNotFoundError("User file " + persistent.playername + "not found. Re-run Setup.")
            
            try:
                with open(config.savedir + "/.causerland/" + persistent.playername, 'r') as data_object:
                    user_data = json.load(data_object)
            except Exception as error:
                user_data = { "name": persistent.playername, "prettyName": persistent.playername }
                
            user_data[bundle_id] = data.copy()
                
            with open(config.savedir + "/.causerland/" + persistent.playername, 'w+') as file:
                json.dump(user_data, file)