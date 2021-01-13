#  Bootloader

![Bootloader logo](../images/system/bootloader.png)

The bootloader is responsible for displaying a boot screen while important components are loading. The bootloader is cusomizable with a certain timeout, depending on how fast you want the OS to "load".

## Available methods

### `$ ASBootloader.boot(timeout=5, expressSetup=True, disclaimer=None, bootView="ASBootloaderView")`

Show the bootloader for a certain amount of time.

**Parameters**

- `timeout`: The amount of seconds to show the bootloader for.
- `expressSetup`: Whether the Setup Assistant should start in Express Mode.
- `disclaimer`: Any license agreement or disclaimer that must be displayed during the Setup Assistant.
- `bootView`: The name of the Ren'Py screen to display as the GUI for the boot loader.
