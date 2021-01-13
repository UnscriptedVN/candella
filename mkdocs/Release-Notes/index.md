#  Prospect Park (2.0.0)

The following document covers the latest changes in AliceOS Prospect Park (v. 2.0.0). If you are upgrading from Developer Beta 3, you can read the [latest changes since that release](#changes-since-developer-beta-3).

!!! info "Before you upgrade"
    AliceOS Prospect Park is a dramatic overhaul of the classic AliceOS and may break upon installation. Please review everything carefully.

## General

- The system organization has migrated over to a macOS-styled directory structure with System, Library, and Applications.
- Installation has changed over to an RPA-based solution. Installation now is as simple as dragging the RPA.
- AliceOS APIs, class names, and function names have been renamed and switch over to camel case instead of snake case.

## Apps

- Applets have been deprecated in favor of new apps written with AppKit in mind.
- Apps no longer need to declare a desktop shell component as this is handled by the native `applicationWillLaunch` method.
- Apps can now write starup/login services via `applicationWillLaunchAtLogin()` and check for System Events permissions with `applicationShouldLaunchAtLogin()`.
- Notifications and alerts in AppKit are now invoked in a new context instead of interrupting the current one.
- The 48 pixel icon entry in `ASAppRepresentative` has been re-added.
- If unimplemented, `applicationWillLaunch()` will log a warning in the terminal.
- Introduces a new Inventories app, a fast and fun way to create and manage a game inventory.

## Messages

- Messages now displays a "Coming Soon" alert when launched from the Desktop.


## Core Services and Applications

- Applications such as Messages have been moved to `System/Applications/` and use AppKit.
- The halt screen, bootloader, and Setup Assistant are now Core Services that use ServiceKit.

## Desktop

- The Desktop now uses the `applicationWillLaunch` method from AppKit apps to start apps accordingly and will invoke `applicationWillLaunch` as a Ren'Py function callback.
- The Desktop image is defined as `AS_DESKTOP_IMG`.
- The Desktop now refreshes quickly to get the latest time on the clock.

## Halt screens (formerly Stop errors)

- The halt screen uses the AliceOS dynamic blur instead of its own background.
- A QR code has been added that redirects users to the AliceOS Error Database.
- The text has been changed to indicate how long before AliceOS will automatically restart the game.

## Notifications

- Notifications are now under the NotificationKit framework.
- Alerts no longer appear as a white square. They now use the AliceOS dynamic blur feature.

## Bootloader

- The bootloader will now attempt to run any authorized startup services in a new thread.
- An optional `bootView` parameter allows developers to set a custom boot screen to display instead of the default.

## Setup Assistant

- Express Mode is on by default, but can be disabled in the bootloader's `boot` method.
- Instructions have been rewritten for conciseness and clarity.
- The interface has changed to a more macOS-like experience.
- Setup Assistant now uses ScreenKit to draw elements.

## ScreenKit

- ScreenKit has been introduced as a means of creating user interfaces for AliceOS using Ren'Py's screen language and styling.
- Styles for frames, vertical and horizontal boxes, text, checkbox buttons, vertical scrollbars, and push buttons have been implemented.
- `ASInterfaceTitlebar` has been implemented as a smaller component to add a title bar to a given frame.
- ScreenKit now include horizontal scrollbars and radio buttons.
- ScreenKit frames are more rectangular.

## About AliceOS

- The main interface has been written entirely with ScreenKit and displays information from system definitions.
    - The Ren'Py version should now match the proper built version and not be hard-coded.

## App Manager

- App Manager has been introduced as a means of managing an app's permissions and viewing details about the app.
- Apps in App Manager list their permissions as toggleable checkboxes.


## Changes since Developer Beta 3

### Inventories

- `ASInventoryItem` objects can now have an optional ID field, `itemId`.
- `ASInventories` includes new methods:
    - `export(filter=None)`: Return the inventory with a filter, if specified.
    - `getItemById(itemId)`: Find an item by its ID.

### AppKit

- Permission strings now reference App Manager instead of Settings.

### Desktop

- `showDesktop()` now calls `renpy.show_screen` instead of `renpy.call_screen`. For the old behavior, reference `_callDesktop()`.

### CI/CD

- AliceOS now produces builds on every push/pull request that can be accessed on GitHub Actions.

!!! warning
    Treat these builds from GitHub as a developer release; do _not_ use these builds in production-ready visual novels.