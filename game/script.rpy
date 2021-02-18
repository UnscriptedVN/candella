# Run the bootloader.

label splashscreen:
    $ roland.boot(loader="RolandGraphicalLogomarkLoader", minimum_load_time=3.0)
    return

# Run the bootloader's shutdown.

label quit:
    $ roland.shutdown(loader="RolandTextLoader")
    return

# Open the desktop.

label start:
    $ celeste.launch()
    return

# Show an example Stop screen.

label example_halt:
    python:
        ASHalt.halt("DEMO_REQUEST_HALT")
        renpy.utter_restart()
    return

# Force-restart the Setup Assistant.

label reset:
    python:
        persistent.AS_COMPLETED_SETUP = False
        renpy.utter_restart()
    return
