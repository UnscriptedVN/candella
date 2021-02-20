# Writing core services

In addition to writing custom apps, Candella offers support for writing custom core services that other apps can rely on. Core services are handled by the `CACoreService` class and function similarly to Candella apps. Core services also inherit the properties of `CAObservable`, allowing it to emit signals to observers.

## Creating a core service

The recommended way of creating a core service from scratch is to use the Candella SDK and follow the interactive prompts:

```
candella-sdk --action create --type service
```

Likewise, you can also follow the instructions below to make a core service manually:

1. Create a folder with the structure `YourAppName.aosapp` inside of the System/CoreServices folder.
2. Create a manifest file inside of the service folder using the manifest structure (see ["The manifest file"](#the-manifest-file)).
3. Create the `Resources/Iconset` folders inside of the service directory.
4. Add service icons for the following sizes in pixels (their names will be the corresponding size): 16, 24, 32, 48, 64, 128, 256, 512, 1024.
5. Create a file with your service's name with the `rpy` extension. Use the template below to fill the contents of your service.

```rpy
#
# ServiceName.rpy
# Service Name
#
# (C) Year Author.
#

init offset = 5
init python:
    class Service(CACoreService):
        """Service description"""


        def __init__(self):
            CACoreService.__init__(
                self,
                AS_CORESERVICES_DIR + "ServiceName.aoscservice/"
            )

            # Initialize your core service here.

    # Initialize the service outside of the class.
    service = Service()
```

## The manifest file

Like Candella apps, core services also include a manifest file that defines the service, as well as its permissions and requisites. This is also located in the root of the service folder and should be named `manifest.json`.

| Field | What it does |
| ----- | ------------ |
| `name` | A short name of your service. |
| `id` | An identifier for the service. It is recommended to use reverse domain notation. |
| `author` | The author of the service. It is recommended to use the `Name <name@email.server>` format. |
| `version` | The current version of the service. |
| `description` | A summary of what your service does. |
| `license` | The license your service falls under as an SPDX expression. |
| `permissions` | A list of strings containing what permissions your service requires. See [permissions in the app manifest](./03-candella-app.md#manifest-permissions). |
| `requisites` | (Optional) A list of strings containing the names of the frameworks this service relies on. |

!!! warning "Unrestricted access"
    Core services typically have unrestricted access to resources, unlike Candella apps, when declared in the manifest. Ensure that you declare only the permissions you need and that you use those resource wisely.

### Validating service requisites

Core services that depend on requisite frameworks should be declared in the app's manifest under the `requisites` field. At initialization time, the service will determine whether or not the frameworks are present.

## Core service lifecycle

Like Candella apps, core services have a lifecycle based on the structure of AliceOS core services. These methods are called when a stage of the service lifecycle will happen and when the stage has finished; for launch, this would be `ASCoreServiceRepresentative.serviceWillLaunch` and `ASCoreServiceRepresentative.serviceDidLaunch`, respectively. The same applies for when an service's termination cycle.

Candella services can still hook into these methods by defining similar methods:

- For launch, `CACoreService.service_will_launch` and `CACoreService.service_did_launch`.
- For teardown, `CACoreService.service_will_terminate`.

Candella services also have two new methods at their disposal that make calls to these methods:

- `CACoreService.launch` for launch stages in the services's lifecycle.
- `CACoreService.terminate` for termination stages.

Whether you want to use the AliceOS-style approach or the new launch/terminate approach is up to you, but remember to keep your logic in a consistent order. If you decide to override the latter methods, be sure to emit the appropriate signals:

- In `launch`, `emit_signal("service_launched", name=self.__class__.__name__)`
- In `terminate`, `emit_signal("service_terminated")`

## Sending service signals

Core services have the ability to emit signals, just like Candella apps; more information on signals can be found in the [documentation about the Observable framework](./04-observable.md).

By default, core services emit the following signals:

| Signal | Arguments | Purpose |
| ------ | --------- | ------- |
| `service_launched` | `name=self.__class__.__name__` | Indicates that the service launched successfully. |
| `service_launched_at_login` | `name=self.__class__.__name__` | Indicates that the service launched during boot successfully. | 
| `service_terminated` | None | Indicates the service was terminated successfully. |
| `service_requested_notification` | `response=response` | Indicates that the service sent a notification request and received a response from the user. |

## Service storage

Like apps, core services also have access to containerized storage for the currently logged-on user. Details on how to use service storage can be found in the [Multiuser framework documentation](./05-multiuser.md#readingwriting-data-for-the-current-user).