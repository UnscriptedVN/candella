# Run the bootloader.

label splashscreen:
    $ ASBootloader.boot()
    return

# Open the desktop.
    
label start:
    $ ASDesktop._callDesktop()
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