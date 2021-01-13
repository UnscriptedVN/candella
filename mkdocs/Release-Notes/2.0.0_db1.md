#  Prospect Park (2.0.0) Developer Beta 1

The following document covers the latest changes in AliceOS Prospect Park (v. 2.0.0).

!!! warning "This document is not complete"
    More documentation is being worked on with this document to describe exact changes.

!!! info "Before you upgrade"
    AliceOS Prospect Park is a dramatic overhaul of the classic AliceOS and may break upon installation. Please review everything carefully.

## General

- The system organization has migrated over to a macOS-styled directory structure with System, Library, and Applications.
- Installation has changed over to an RPA-based solution. Installation now is as simple as dragging the RPA.
- AliceOS APIs, class names, and function names have been renamed and switch over to camel case instead of snake case.

## Apps

- Applets have been deprecated in favor of new apps written with AppKit in mind.
- Apps no longer need to declare a desktop shell component as this is handled by the native `applicationWillLaunch` method.

## Core Services and Applications

- Applications such as Messages have been moved to `System/Applications/` and use AppKit.
- The halt screen, bootloader, and Setup Assistant are now Core Services that use ServiceKit.

## Desktop

- The Desktop now uses the `applicationWillLaunch` method from AppKit apps to start apps accordingly.
- The Desktop image is defined as `AS_DESKTOP_IMG`.
- The Desktop now refreshes quickly to get the latest time on the clock.

### Known issues

- The Desktop doesn't hide the quick menu.
- The `showDesktop()` method from `ASDesktop` doesn't work in Ren'Py screen language.

### Workarounds

- Call `ASDesktopShell` directly instead of using the `showDesktop()` method.

## Halt screens (formerly Stop errors)

- The halt screen uses the AliceOS dynamic blur instead of its own background.
- A QR code has been added that redirects users to the AliceOS Error Database.
- The text has been changed to indicate how long before AliceOS will automatically restart the game.

## Notifications

- Notifications are now under the NotificationKit framework.
- Alerts no longer appear as a white square. They now use the AliceOS dynamic blur feature.

### Known issues

- Notification banners do not make a sound.

## Setup Assistant

- Express Mode is on by default, but can be disabled in the bootloader's `boot` method.
- Instructions have been rewritten for conciseness and clarity.
- The interface has changed to a more macOS-like experience.
