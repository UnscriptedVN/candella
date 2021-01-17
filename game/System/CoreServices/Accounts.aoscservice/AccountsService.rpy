#
# AccountsService.rpy
# Candella Accounts Service
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -10

init python:
    import os
    
    class CAAccountsUserNotFoundError(Exception):
        """The specified user was not found."""
    
    class CAAccountsService(ASCoreServiceRepresentative):
        bundleName = "Accounts Service"
        bundleId = "dev.unscriptedvn.candella.accounts-service"
        bundleDir = AS_CORESERVICES_DIR + "Accounts.aoscservice/"
        bundleAuthor = "Unscripted VN Team <unscriptedvn@marquiskurt.net>"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Manage multiple user accounts via the Multiuser framework.
        """
        
        _accounts_dir = config.savedir + "/.causerland"
        _users_list = []
        
        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Accounts.aoscservice/")
            self._users_list = CAAccountsService.get_all_users()
        
        @staticmethod
        def get_logged_in_user():
            """Returns the user information for the currently logged in user."""
            _user = CAUserData(persistent.playername)
            return CAUser(_user.data["name"], _user.data["prettyName"])
        
        @staticmethod
        def get_all_users():
            """Returns a list of user objects."""
            users = []
            for name in os.listdir(config.savedir + "/.causerland"):
                users += [CAAccountsService._get_user(name)]
                return users
        
        @staticmethod
        def _get_user(username):
            """Returns the user information for a specified user.
            
            Arguments:
                username (str): The username of the user to get.
            
            Returns:
                user (CAUser): The user information.
            
            Raises:
                If the user doesn't exist in the userland folder, a CAAccountsUserNotFoundError is raised.
            """
            if username not in os.listdir(config.savedir + "/.causerland"):
                raise CAAccountsUserNotFoundError(username)
            _data = CAUserData(username)
            return CAUser(_data._data["name"], _data._data["prettyName"])
            
        def add_user(self, username, pretty_name=None):
            """Creates the user file for a given user and adds it to the user list.
            
            Arguments:
                username (str): The username for the new user.
                pretty_name (str): The display name for the new user.
            """
            CAUserData._create_user_file(username, pretty_name=pretty_name)
            _users_list = CAUser(username, pretty_name)
            
        def remove_user(self, username):
            """Removes the specified user.
            
            Arguments:
                username (str): The username of the user to remove.
            """
            try:
                os.remove(_accounts_dir + "/" + username)
                for user in self._users_list:
                    if user.username != username:
                        continue
                    self._users_list.remove(user)
            except:
                pass