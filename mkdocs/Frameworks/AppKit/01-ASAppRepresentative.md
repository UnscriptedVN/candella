# ASAppRepresentative

`ASAppRepresentative` is the Python class responsible for defining apps in AliceOS. This class acts as the app's delegate and information manifest. The following documentation covers all of the methods and properties of this class.

## Properties

- `bundleName`: The name of the application.
- `bundleId`: The ID of the application in [reverse domain name notation](https://en.wikipedia.org/wiki/Reverse_domain_name_notation).
- `bundleDir`: The location of the application. By default, apps use `AS_APPS_DIR + "<applicationname>.aosapp/"`.
- `bundleAuthor`: The author or organization that developed the application.
- `bundleVersion`: The version of the application.
- `bundleDescription`: The description of the application.
- `requires`: A dictionary containing all of the permissions needed for the app to function.
- `icons`: A dictionary containing the paths of all icons for the appropriate sizes.

## Methods

### `__init__(appDirectory)`

Constructs an instance of `ASAppRepresentative`.

**Parameters**

- `appDirectory`: The directory of which the app is located. Equivalent to `bundleDir`.

### `requestPermission(forPermission)`

Requests a particular permission located in `requires`.

**Parameters**

- `forPermission`: The permission to request. Must be in `requires` to execute.

### `requestAllPermissions()`

Requests all permissions located in `requires`, one by one.

### `applicationShouldLaunchAtLogin()`

Returns whether the app is authorized to run any login tasks.

### `applicationWillLaunchAtLogin()`

Executes and preliminary actions during the boot sequence.

### `applicationWillLaunch()`

Executes any preliminary actions before the app launches.

### `applicationDidLaunch()`

Executes post-launch actions after the app has launched.

### `applicationWillTerminate()`

Executes cleanup actions before the app closes.

### `applicationDidTerminate()`

Executes any tasks before finally closing.

### `applicationShouldRequestNotification()`

Return whether the app is authorized to send notifications.

**Returns**

Boolean value dictating whether the app includes the notification permission and has permission to send notifications from the user.

### `applicationWillRequestNotification(message, withDetails, responseCallback)`

Executes any pre-processing for a notification request and then sends a request.

**Parameters**

- `message`: The message or title of the notification.
- `withDetails`: The details of the notification.
- `responseCallback` (Optional) The action to perform when clicking 'Respond'.

### `applicationDidRequestNotification()`

Executes any actions after sending a notification request.

### `applicationWillRequestBasicAlert(message, withDetails, onDismissCallback)`

Executes any pre-processing for an alert and then sends an alert request.

**Parameters**

- `message`: The message or title of the alert.
- `withDetails`: The details of the alert.
- `onDismissCallback` (Optional) The action to perform when clicking 'OK'.

### `applicationWillRequestExtendedAlert(message, withDetails, primaryActionText, onPrimaryCallback, secondaryActionText, onSecondaryCallback)`

Executes any pre-processing for an extended alert and then sends an alert request.

- `message`: The message or title of the alert.
- `withDetails`: The details of the alert.
- `primaryActionText`: The text for the primary action button
- `onPrimaryCallback` (Optional) The action to perform when clicking the primary button.
- `secondaryActionText`: (Optional) The text for the secondary action button
- `onSecondaryCallback` (Optional) The action to perform when clicking the secondary button.

### `applicationDidRequestAlert()`

Executes any actions after sending an alert.
