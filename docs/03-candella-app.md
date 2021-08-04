# Writing a Candella app

Candella includes support for writing miniature apps that work within the Candella system. These apps sit on top of the [AppKit][appkit] framework for AliceOS (not to be confused with Apple's AppKit) and are backwards-compatible with AppKit APIs.

## Creating an app

Candella apps are built in the same fashion as AliceOS apps by creating a directory with the `aosapp` extension in the `Applications` folder of a Ren'Py project.

With the Candella SDK, you can run the following to interactively generate a project for you. The SDK will automatically create the structure and provide default icons for you. 

To do so, run the following:
```bash
candella-sdk --action create --type application
```

Alternatively, you can follow the instructions provided:

1. If the Applications folder doesn't exist already, create it inside of the `game` directory.
2. Create a folder with the structure `YourAppName.aosapp` inside of the Applications folder.
3. Create a manifest file inside of the app folder using the manifest structure (see ["The manifest file"](#the-manifest-file)).
4. Create the `Resources/Iconset` folders inside of the app directory.
5. Add app icons for the following sizes in pixels (their names will be the corresponding size): 16, 24, 32, 48, 64, 128, 256, 512, 1024.
6. Create a file with your app's name with the `rpy` extension. Use the template below to fill the contents of your app.

```rpy
#
# AppName.rpy
# Application
#
# (C) Year Author.
#

init offset = 10
init python:
    class AppName(CAApplication):
        def __init__(self):
            CAApplication.__init__(self, app_path=AS_APPS_DIR + "AppName.aosapp/")
        
    appname = AppName()
```

### The manifest file

The manifest file contains information about your app, as well as what the app needs from Candella to run. The manifest file is located in the root of the app as `manifest.json`. Candella will automatically fill in the information of the app for you as the Ren'Py project initializes.

| Field | What it does |
| ----- | ------------ |
| `name` | A short name of your app. This can also be used as the command name. |
| `productName` | (Optional) A human-readable version of the app name. |
| `id` | An identifier for the app. It is recommended to use reverse domain notation. |
| `author` | The author of the app. It is recommended to use the `Name <name@email.server>` format. |
| `version` | The current version of the app. |
| `description` | A summary of what your app does. |
| `license` | The license your app falls under as an SPDX expression. |
| `permissions` | A list of strings containing what permissions your app requires. See [permissions in the app manifest](#manifest-permissions). |
| `requisites` | (Optional) A list of strings containing the names of the frameworks this app relies on. |
The following is an example manifest: |

```json
{
    "name": "textedit",
    "productName": "Text Editor",
    "id": "com.appleseed.text-editor",
    "author": "John Appleseed <john@appleseed.email>",
    "version": "12.0.0",
    "description": "A simple text editor for Candella.",
    "license": "GPL-3.0",
    "requires": ["file_system"]
}
```

#### Manifest permissions

The following is a list of the available permissions for apps and core services.

| Permission name | What it grants |
| - | - |
| `file_system` | Requires access to the Candella "file system" |
| `notifications` | Requires access to NotificationKit to send notifications |
| `system_events` | Requires access to System Events |
| `manage_users` | Requires access to the accounts service to manage users |
| `virtual_platform` | Requires access to the MeteorVM platform |


## App lifecycle

In AliceOS, there are methods that exist for apps for launch and teardown. These methods are called when a stage of the app lifecycle will happen and when the stage has finished; for launch, this would be `ASAppRepresentative.applicationWillLaunch` and `ASAppRepresentative.applicationDidLaunch`, respectively. The same applies for when an app's termination cycle.

Candella apps can still hook into these methods by defining similar methods:

- For launch, `CAApplication.application_will_launch` and `CAApplication.application_did_launch`.
- For teardown, `CAApplication.application_will_terminate` and `CAApplication.application_did_terminate`.

Candella apps also have two new methods at their disposal that make calls to these methods:

- `CAApplication.launch` for launch stages in the app's lifecycle.
- `CAApplication.terminate` for termination stages.

Whether you want to use the AliceOS-style approach or the new launch/terminate approach is up to you, but remember to keep your logic in a consistent order. If you decide to override the latter methods, be sure to emit the appropriate signals:

- In `launch`, `emit_signal("application_launched", name=self.get_name())`
- In `terminate`, `emit_signal("application_terminated")`

More information on AliceOS's app lifecycle can be [found on the AliceOS documentation][app-lifecycle].

### Validating app frameworks

If your Candella app requires frameworks and you want to check that those frameworks are available, you can add the `requisites` field to your manifest file. The `requisites` field takes a list of strings containing the framework names that are required for your app to run.

Most apps by default will have a requisite list of `["AppKit", "Observable"]`.

## Convenience methods

Candella apps also include some methods to make gathering values a lot easier. These methods can be used to get the app's name or app icon; they are generally used in conjunction with services such as desktop shells.

### `CAApplication.get_name()`
Returns the name of the app, or its bundle name.

### `CAApplication.get_app_icon(size=16)`
Returns the path for a given icon size.

## App storage

Apps can also store data for the currently logged-in user on the system; this data can be used to save preferences or other data that is necessary for app functions. App storage is handled by the `AppStorage` class and can be accessed for your app via `CAApplication.data`.

!!! warning "Declare file system permissions"
    Apps that utilize app storage must include the `file_system` permission in their app manifest in the `permissions` field. Apps will not be able to access app storage if this permission isn't declared or if the user has not granted the app permission to do so.

There are three methods in `AppStorage` to help read and write data accordingly:

- `AppStorage.get_entry(field, raise_falsy=False)` will fetch the value for a field or return `None` if no value for the field was found. If `raise_falsy` is set to `True`, the method will instead raise an exception.
- `AppStorage.set_entry(field, value)` will write the value `value` into the specified `field`.
- `AppStorage.commit()` will commit all written changes to the current user's data file.

!!! danger "Sensitive Information"
    Do _**not**_ store sensitive information in app storage unless you are using cryptography to encrypt the information. App storage is provided in the user's data file in a human-readable format and may be easily compromised if not encrypted properly.

## User interfaces

User interfaces for Candella apps utilize ScreenKit, an AliceOS framework that uses Ren'Py screen language to construct consistent user interfaces that match the system.

More information on generating user interfaces with ScreenKit [can be found in the AliceOS documentation][screenkit].

### Creating draggable windows

It is recommended that, if possible, to give your app windows the ability to be dragged across the screen. This can be achieved by wrapping the window's content in a `drag` screen, supplying the following properties like in the example below:

```rpy
drag:
    drag_name "NameOfScreenGoesHere"
    drag_handle (0, 0, WindowMaxWidthHere, 64)
    xalign 0.5
    yalign 0.5

    ...
```

- `drag_name` should contain the name of the screen your app's window resides in
- `drag_handle` will set the draggability from the title bar. We recommend keeping the default values of 0, 0 for the X and Y values, as well as setting the last value (height) to 64px. The third element in the tuple should correspond to the width of the window.
- Other transform properties on the alignment must also appear in the draggable to set the default position. In most cases, this is in the center of the screen.

!!! important "Remember window modality rules"
    Keep in mind your window's modality when making the window draggable. Windows in Candella should not be draggable if they are modal (`modal True` in screen properties) unless there is a backdrop behind it. Leaving a window with draggable properties as a modal window may cause unexpected issues for players when trying to rearrange other windows.

## Sending notifications

Candella offer two types of notifications: banners and alerts. Sending a banner or alert is easy with a simple method call. These method calls handle notification delegates and permission requests for you and will return the response provided, as well as emit it in a signal.

### `CAAplication.send_alert(title, details, callback=Return('didDismissAlert'))`
Send an alert with respect to the user's settings.

**Arguments**

- title (str): The title of the alert.
- details (str): The supporting text or details for the alert.
- callback (callable): The response callback function to run when dismissing the alert.

**Returns**

- response (any): The response from the alert, if any. This response is also emitted as a signal.

### `CAApplication.send_banner(title, supporting, callback=Return('didClickRespond'))`
Send a notification banner with respect to the user's settings.

The banner request can be used in one of two ways: automatic, which utilizes the CANotificationBanner class
    to create a notification banner, and manual, which uses keyword arguments at call time to generate a
    banner on the fly. In most cases, it is recommended to use the automatic mode since the
    CANotificationBanner class offers more granular control over the appearance of the banner such as the
    action button text.

**Arguments**

- mode (str): The means of sending the request. 'automatic' utilizes the [`CANotificationBanner`](./11-notifications.md#creating-modular-banners-labelnew) class to
    create a banner, and 'manual' uses to the old style. By default, this method uses manual mode to
    ensure backwards-compatibility with AliceOS and older Candella versions.

**Keyword Arguments**

- banner (CANotificationBanner): The banner object to send through this app. Required in automatic
    mode.
- title (str): The title of the banner. Required in manual mode.
- supporting (str): The supporting text for the banner. Required in manual mode.
- callback (callable): The response callback function to run when clicking the 'Respond' button. Required
    in manual mode.

**Returns**

- response (any): The response from the banner request, if any.

!!! warning "Add keyword arguments"
    For Candella apps that use the manual mode or have supplied the contents of the banner as arguments, make sure that these are changed to keyword arguments, appropriately.
## Sending app signals

Apps can send information to other services and even other apps. Candella apps adopt the Observable framework, which allows for signal emission.

To emit a signal from your app, use the `emit_signal` method, followed by what you want to send.

For instance, if you have an arcade shooter game `ArcadeShooter` and wanted to emit a signal to any receivers with an updated score:

```py
class ArcadeShooter(CAApplication):
    # ...
    def submit_score(self, score=0):
        self.score = score

        # Emit a signal with the updated score.
        # Apps and services that are listening to this
        # signal can access the score with kwargs["score"].
        self.emit_signal("score_submitted", score=score)
```

The following signals are emitted by default:

| Signal | Arguments | Purpose |
| ------ | --------- | ------- |
| `application_launched` | `name=self.get_name()` | Indicates that the application launched successfully. |
| `application_launched_at_login` | `name=self.get_name()` | Indicates that the application launched during the boot process successfully. |
| `application_terminated` | None | Indicates that the application terminated successfully. |
| `banner_sent` | `response=any` |  Indicates that the application sent a banner notification request and received a response from the user. |
| `alert_sent` | `response=any` |  Indicates that the application sent an alert notification request and received a response from the user. |

## `CAApplication`

`CAApplication` is the primary class used to create Candella apps. It is an extension of the standard `ASAppRepresentative` class and aims to make app development simpler. This class provides extra utilities to simplify app development.

### Differences Between `ASAppRepresentative`
- Apps do not need to override class attributes to fill out app metadata. Instead, this is achieved with
    a manifest file, manifest.json.
- Notification requests are handled by methods that simplify calls.
- Grabbing icon sizes for an app is handled with a method.
- The description field for the app includes information regarding AliceOS compatibility.
- The license, product name, permissions, and description fields are present.
- This class contains methods for accessing user data via the Multiuser framework.
- This class inherits the `CAObservable` class, which will emit signals to services or apps that listen for
    it.

### Class Attributes
- description (str): The description for the app (same as bundleDescription).
- product_name (str): The human-readable name of the app.
- license (str): The license this app falls under.
- permissions (list): A list containing all of the permissions this app needs.
- data (AppStorage): An app storage object for this app, or None if the app doesn't need app storage.

[appkit]: https://docs.aliceos.app/Frameworks/AppKit/
[app-lifecycle]: https://docs.aliceos.app/Frameworks/AppKit/01-ASAppRepresentative/#applicationshouldlaunchatlogin
[screenkit]: https://docs.aliceos.app/Frameworks/ScreenKit/