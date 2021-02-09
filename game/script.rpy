# Run the bootloader.

label splashscreen:
    $ roland.boot(loader="RolandGraphicalLoader", minimum_load_time=1.0)
    return

# Run the bootloader's shutdown.

label quit:
    $ roland.shutdown(loader="RolandGraphicalLoader")
    return

# Open the desktop.

label start:
    $ caberto.launch()
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
