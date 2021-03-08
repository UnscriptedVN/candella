# Multiuser Framework

Multi-user support in Candella is provided by the Multiuser framework. This framework adds the necessary classes and utilities to create and manage multiple users, as well as manage data for specific users.

## What is a Candella user?

A user is defined by a username and is represented as the `CAUser` data class. In most cases, developers will not need to create an instance of this class as core services and applications will provide this automatically.

- `CAUser.username` contains the username of the user. Usernames must be in lowercase with no spaces or special characters.
- `CAUser.display_name` contains the user-facing display name for the user. This display name is used by core services such as Celeste Shell to display the user's name. By default, this name defaults to the username.

`CAUser` provides methods for checking equality and string representation.

## The userland folder

Each user gets a corresponding file in the `.causerland` directory. This directory is located in the save directory of the Ren'Py project. For instance, if Candella were installed in _Doki Doki Literature Club!_, the userland folder is located at the following path:

```
%AppData%\RenPy\DDLC\.causerland # Windows
~/Library/RenPy/DDLC/.causerland # macOS
~/.renpy/DDLC/.causerland # Linux
```

Users and app/service developers typically don't need to worry about the user file as classes exists for managing data in the userland folder.

## Reading/writing data for the current user

Apps and services provide their own means of accessing sandboxed data. These classes ensure that the app or service can locally access only their data. App/service data is registered under its bundle ID.

### `AppStorage`

For Candella apps, the `AppStorage` class is used to manage data. More information using AppStorage can be [found in the documentation for creating Candella apps][caapplication].

### `ServiceStorage`

Likewise, core services in Candella utilize the `ServiceStorage` class. Like `AppStorage`, data is separated by bundle ID and is accessible via the `data` field of the `CACoreService` class.

There are three methods available for managing service data:

- `ServiceStorage.get_entry(field, raise_falsy=False)` will fetch the value for a field or return `None` if no value for the field was found. If `raise_falsy` is set to `True`, the method will instead raise an exception.
- `ServiceStorage.set_entry(field, value)` will write the value `value` into the specified `field`.
- `ServiceStorage.commit()` will commit all written changes to the current user's data file.

!!! danger "Sensitive Information"
    Do _**not**_ store sensitive information in service storage unless you are using cryptography to encrypt the information. Service storage is provided in the user's data file in a human-readable format and may be easily compromised if not encrypted properly.

### Global scope access

There may be instances where you need to access application data outside of the app class. There are two static methods in the `CAUserData` class to handle this:

#### `CAUserData.get_current_user_data(bundle_id)`
Returns the application data for the current user.

**Arguments**

- bundle_id (str): The app's bundle ID.

**Returns**

- app_data (dict): The user data for the specified app as a dictionary. If no data was found for the app, an empty dictionary will be returned.

**Raises**

If the app doesn't have permissions to open the data, CAUserDataPermissionError is raised.
    If the user file doesn't exist, FileNotFoundError is raised. Otherwise, any other
    exceptions from file opening and parsing may be thrown.

#### `CAUserData.write_data_to_current_user(bundle_id, data={})`
Writes the specified app data to the current user's file.
            
**Arguments**

- bundle_id (str): The app's bundle ID
- data (dict): The data to write to the file for that bundle ID.

**Raises**

If the app doesn't have permissions to write the data, CAUserDataPermissionError is raised.
    If the user file doesn't exist, FileNotFoundError is raised. Otherwise, any other
    exceptions from file opening and writing may be thrown.

[caapplication]: ./03-candella-app.md#app-storage