# Accounts Service

The **Accounts Service** for Candella extends the functionality of the Multiuser framework and adds support for managing users in a way that lets other services handle this functionality. This service defines a single class, `CAAccountsService`, to manage users efficiently.

!!! note "Backwards Compatibility with AliceOS"
    To maintain backwards compatibility with AliceOS, the username of the currently logged-in user is set in AliceOS's `persistent.playername`. This field is commonly used by services and apps for the current player, and it also defines the player's name in games like _Doki Doki Literature Club!_.

## Viewing information about the userspace

Currently, there are two static methods available to get information about the userspace:

- `CAAccountsService.get_logged_in_user()` returns a `CAUser` object that contains the information about the currently logged-in user.
- `CAAccountsService.get_all_users()` returns a list of `CAUser` objects that contain information about all users known to Candella in the userspace.

## Managing users

While accessing user information is static and does not require instancing, `CAAccountsService` should be instanced in the service or app that requests these features to manage data more efficiently. Including an instance in your service or app ensures that no other services are using that app's copy, and it helps reduce variables in Ren'Py's store.

!!! warning "Declare user permissions"
    For an app or service to manage users, the `manage_users` permission must be enabled for that service or app. This can be defined in the `permissions` field in an app's manifest and the `requisites` field in a service's manifest, respectively.

To instantiate an instance of the account manager, you'll need to pass in the service or app instance with the `manage_users` permission:

```py
class SampleCoreService(CACoreService):
    def __init__(self):
        CACoreService.__init__(self)
        self._accounts = CAAccountsService(self)
```

### `add_user(self, username, pretty_name=None)`

Creates the user file for a given user and adds it to the user list.
            
**Arguments**

- username (str): The username for the new user.
- pretty_name (str): The display name for the new user.

### `change_current_user(self, username)`

Change the currently logged-in user.

**Arguments**

- username (str): The username of the user to switch to.

### `remove_user(self, username)`

Removes the specified user.
            
**Arguments**

- username (str): The username of the user to remove.