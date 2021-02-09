# Roland Boot Manager

Candella utilizes the **Roland Boot Manager** to start and shut down Candella and its apps/services. Roland allows for a modular approach to booting/shutting down services and apps by letting developers select if a boot screen should be displayed, what screen to load during boot, how long to display it for if Roland finishes. The same applies for shutdown.

## Loading the boot manager

Ideally, the boot manager's boot sequence should be loaded into Ren'Py's `splashscreen` label:

```rpy
label splashscreen:
    $ roland.boot()
    return
```

There are two additional parameters that can be passed into the boot function:

- `loader` (str): The name of the Ren'Py screen to display during boot. By default, this is set to `None`, thus not displaying a screen.
- `minimum_load_time` (float): The minimum amount of seconds the boot screen should be displayed if the boot sequence finishes too quickly. By default, this is set to `0.0`.

### Default boot screens

The Roland Boot Manager comes with a few loading screens by default:

- `RolandGraphicalLoader`: A graphical loader with the game's window icon, if the file is present. Otherwise, the Candella logo is displayed.

### Creating a custom loading screen

You can create a standard Ren'Py screen with the `bootloader` tag and a `zorder` of 200 to be displayed by the boot manager. An example is provided below:

```rpy
screen SampleLoader():
    zorder 200
    tag bootloader
    modal False

    add "#000000"

    vbox:
        align (0.5, 0.5)

        text "Loading the system...":
            xalign 0.5
            text_align 0.5
```

!!! important "Important"
    The loading screen should _not_ have any required parameters. The boot manager will not be able to supply arguments to get passed into the loading screen.

## Shutting down Candella with the boot manager

Like with the `boot` method in the `splashscreen` label, the `shutdown` method should be inserted in the `quit` label:

```rpy
label quit:
    $ roland.shutdown()
    return
```

Like the boot method, there is an additional optional argument, `loader`, which displays a Ren'Py screen during the shutdown process; however, the screen does not include a minimum loading time unlike the boot sequence. By default, this value is set to `None`, indicating that no screen will be displayed.