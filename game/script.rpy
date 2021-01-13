label before_main_menu:
    $ ASBootloader.boot()
    return

label main_menu:
    python:
        ASDesktop.showDesktop()
    return

label start:
    $ ASDesktop.showDesktop()
    return