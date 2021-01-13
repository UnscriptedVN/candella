# Watching for Events

Starting with AliceOS Prospect Park, apps can declare and make use of System Events. Apps that want to use system event watching must declare the `AS_REQUIRES_SYSTEM_EVENTS` permission in their manifest and use the appropriate methods outlined in this document.

## What are system events?

Any operation that AliceOS performs such as startup, login, or displaying an error is considered a system event. Apps that have the permission can access the following system events:

- Startup

## Running tasks during boot

Apps using AppKit may want to perform some initialization tasks when AliceOS boots. This can be accomplished by making use of the `applicationWillLaunchAtLogin` method.

### `applicationWillLaunchAtLogin(self)`

Runs any initial tasks or specified startup tasks during boot.

### `applicationShouldLaunchAtLogin(self)`

Determines whether the application has permission to run tasks during boot.

**Returns**: Boolean value dictating if the app has permission to run at boot.

## Suggested documentation

- [ASAppRepresentative](../Frameworks/AppKit/01-ASAppRepresentative.md)
- [Bootloader](../System/05-bootloader.md)