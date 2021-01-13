#  Declaring Your App

Any app for AliceOS has its own manifest and declarations for what the app does. Luckily, defining an app is as easy as writing it directly into the class that all AliceOS apps inherit from.

## Typical app structure

Apps are usually located in `Applications`, inside of the game folder, and have the file extension `.aosapp`. Inside of the file, a Ren'Py script help determine details about the app, and a Resources folder is included to add assets such as icons, images, and definitions.

For instance, if we are creating an app call **Foobanizer**, the structure would look like this:

```
game/
    Applications/
        Foobanizer.aosapp/
            Foobanizer.rpy
            Resources/
                Iconset/
                    16.png
                    24.png
                    32.png
                    48.png
                    64.png
                    128.png
                    256.png
```

Note that the icons are located in `Resources/Iconset/` and have sizes for 16px, 24px, 32px, 48px, 64px, 128px, and 256px. These icons are important as they will appear in notifications, the desktop, and other places that require an icon.

## Writing your app's manifest

AliceOS apps' manifests are included directly inside of their main app delegate, a subclass of `ASAppRepresentative()`. There are several important key field that _should_ be directly written:

- `bundleName`: The name of the application.
- `bundleId`: The ID of the application in [reverse domain name notation](https://en.wikipedia.org/wiki/Reverse_domain_name_notation).
- `bundleDir`: The location of the application. By default, apps use `AS_APPS_DIR + "<applicationname>.aosapp/"`.
- `bundleAuthor`: The author or organization that developed the application.
- `bundleVersion`: The version of the application.
- `bundleDescription`: The description of the application.

Agan, if we wanted to write Foobanizer's manifest, it'd look like this:

```python

init 10 python:

    class Foobanizer(ASAppRepresentative):
        bundleName = "Foobanizer"
        bundleId = "app.aliceos.foobanizer"
        bundleDir = AS_APPS_DIR + "Foobanizer.aosapp/"
        bundleAuthor = "AliceOS Developers"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Generate random foobanized strings on the fly.
        """
...
```

## Declaring permissions

Apps that need to make use of notifications via NotificationKit, modify files, watch system events, etc., must declare their permissions. This is done inside of the class via the `requires` dictionary:

```python

requires = { }
```

The main permissions are:

- `AS_REQUIRES_NOTIFICATIONKIT`: Requires NotificationKit to send notifications
- `AS_REQUIRES_FULL_DISK_ACCESS`: Requires accessing files
- `AS_REQUIRES_SYSTEM_EVENTS`: Requires changing settings or watching for events

!!! warning "Important"
    All AppKit apps must include this field. If you don't need any permissions or aren't using specific frameworks, leave the dictionary empty.

## Rebuilding icons

Icons for AliceOS apps typically reside in the app's Resources folder, though `ASAppRepresentative` may not pick it up at first. To ensure your app's icon locations are updated, make sure you initialize the class, where `<applicationname>` is the name of your app:

```python
def __init__(self):
    ASAppRepresentative.__init__(self,
        AS_DEFAULT_APP_DIR + "<applicationname>.aosapp/")
```

Again, if we wanted to rebuild Foobanizer's icons:

```python
def __init__(self):
    ASAppRepresentative.__init__(self,
        AS_APPS_DIR + "Foobanizer.aosapp/")
```

## Example manifest

Here's what the manifest file for Foobanizer would look like:

```python

# ASAppRepresentative is a Python class.
# Everything must be wrapped in a Python block.
init 10 python:
    class Foobanizer(ASAppRepresentative):
        bundleName = "Foobanizer"
        bundleId = "app.aliceos.foobanizer"
        bundleDir = AS_APPS_DIR + "Foobanizer.aosapp/"
        bundleAuthor = "AliceOS Developers"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Generate random foobanized strings on the fly.
        """
        
        # Foobanizer doesn't require any permissions.
        requires = { }

        def __init__(self):
            ASAppRepresentative.__init__(self, 
                AS_APPS_DIR + "Foobanizer.aosapp/")
                
    # Finally, we create an instance to pre-load.
    foobanizer = Foobanizer()

```

## Suggested documentation

- [`ASAppRepresentative`](../Frameworks/AppKit/01-ASAppRepresentative.md)