#  Prospect Park (2.0.0) Developer Beta 2

The following document covers the latest changes in AliceOS Prospect Park (v. 2.0.0).

## Apps

- Apps can now write starup/login services via `applicationWillLaunchAtLogin()` and check for System Events permissions with `applicationShouldLaunchAtLogin()`.
- Notfications and alerts in AppKit are now invoked in a new context instead of interrupting the current one.
- The 48 pixel icon entry in `ASAppRepresentative` has been re-added.
- If unimplemented, `applicationWillLaunch()` will log a warning in the terminal.

## Messages

- Messages now displays a "Coming Soon" alert when launched from the Desktop.

## Desktop

- Apps on the desktop will invoke `applicationWillLaunch` as a Ren'Py function callback instead of calling the Python function directly to prevent continuous calls.
- The main views in Desktop now have empty parameter lists to resolve linter warnings.


### Known Issues

- The Desktop doesn't hide the quick menu.
- The `showDesktop()` method from `ASDesktop` doesn't work in Ren'Py screen language when calling it as a button action.

### Workarounds

- Use Ren'Py's `Function` call to run `showDesktop()` or make a call directly to the screen.

## Notifications

### Known issues

- Notification banners do not make a sound.

### Workarounds

- Include a sound in your applet and make a wrapper around `applicationWillRequestNotification()`.

## Bootloader

- The bootloader will now attempt to run any authorized startup services in a new thread.
- An optional `bootView` parameter allows developers to set a custom boot screen to display instead of the default.

## ScreenKit

- ScreenKit has been introduced as a means of creating user interfaces for AliceOS using Ren'Py's screen language and styling.
- Styles for frames, vertical and horizontal boxes, text, checkbox buttons, vertical scrollbars, and push buttons have been implemented.
- `ASInterfaceTitlebar` has been implemented as a smaller component to add a title bar to a given frame.

## About AliceOS

- The main interface has been written entirely with ScreenKit and displays information from system definitions.

## App Manager

- App Manager has been introduced as a means of managing an app's permissions and viewing details about the app.
- Apps in App Manager list their permissions as toggleable checkboxes.
