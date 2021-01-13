#  Default Apps

AliceOS includes several default applications that are located in `System/Applications/`. These applications are designed to enhance the AliceOS experience and provide functionalities for core parts without having to write a third-party app for them.

## Messages

![Messages app icon](../images/system/defapps/messages.png)

Messages is a simple app designed to simulate text messaging between characters and the player in a fun way.

**Available methods**

`messages.receiveMessage(fromPerson, message)`

Send a notification request that displays a text message from a person.

**Parameters**

- `fromPerson`: The person the message is being sent from
- `message`: The text message being sent

**Returns**
Returns the default values as indicated from [ASNotificationBanner](../../NotificationKit/01-banner/#returns)

## About AliceOS

![SysInfo icon](../images/system/defapps/sysinfo.png)

About AliceOS is a simple app that displays information about the current distribution of AliceOS. Users can click on the app in Activites and view the information there.

There are no available methods as the app uses the standard `applicationWillLaunch` method from AppKit.

## App Manager

![AppManager icon](../images/system/defapps/appman.png)

App Manager is a(n) utility in AliceOS that lets users view the apps installed on the AliceOS system and manage their permissions quickly. It is the official method of changing an app's permissions in AliceOS.

There are no available methods as the app uses the standard `applicationWillLaunch` method from AppKit.

## Inventories

![Inventories icon](../images/system/defapps/inventories.png)

Inventories is a tool for AliceOS that lets developers and players work with an inventory.

More information on Inventories can be found in the [Inventories documentation](07-inventories.md).