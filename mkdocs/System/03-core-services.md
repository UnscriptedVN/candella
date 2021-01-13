#  Core Services

AliceOS comes with several bundled Core Services that you should be aware of. These Core Services are crucial to AliceOS's core and are included in every AliceOS installation. Core Services are given the `.aoscservice` file extension and exist under `System/CoreServices`. Core services also make use of ServiceKit, an in-house framework for defining core services.

!!! danger "About ServiceKit"
    At all costs, do not remove **ServiceKit.aosframework** or attempt to write your own applications using ServiceKit. ServiceKit is a service-only API set that should be used for system-level utilities, not for third-party applications. Use [AppKit](../Develop-Apps/index.md) instead.

## Desktop

![Desktop icon](../images/system/cservices/desktop.png)

The Desktop Core Service is responsible for displaying current applications installed on the system as well as providing a desktop shell if necessary.

## Error Halt System

![Halt icon](../images/system/cservices/halt.png)

The Error Halt System (Halt) Core Service is responsible for displaying any critical errors that cause AliceOS to restart. It provides helpful information such as the error code and where to go for more information.

More information on how this Core Service works can be found on the article about [Critical Errors](./04-critical-errors.md).

## Bootloader

![Bootloader icon](../images/system/cservices/boot.png)

The Bootloader is responsible for displaying a boot screen while important components are loading. The bootloader is cusomizable with a certain timeout, depending on how fast you want the OS to "load". If the Setup Assistant hasn't fired or completed, the bootloader will also load the Setup Assistant.

## Setup Assistant

![Setup Assistant icon](../images/system/cservices/setup.png)

The Setup Assistant is responsible for setting up any important configurations and settings for AliceOS, as well as creating a username stored in `persistent.playername` and letting users read any legal agreements before playing a visual novel project.

## Removing a service

If you find that you don't need a particular core service, you can delete it from the `CoreServices` directory and rebuild AliceOS.

!!! warning
    If you plan to remove a Core Service, do so with caution. Other parts of AliceOS may make system calls that heavily rely on them.
