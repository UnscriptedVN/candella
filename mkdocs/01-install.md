#  Installing AliceOS

This document will help you get started with installing AliceOS and attaching it to your Ren'Py project.

## Downloading the base system

If you do not plan to customize AliceOS too much, you can add the base system archive and use AliceOS that way.

Download the latest release from the Downloads page and extract the ZIP archive. Then, copy `AliceOSBaseSystem.rpa` over to your Ren'Py project's game folder.

!!! info "Ensure compatibility"
    The latest version of AliceOS for download will always correspond to the latest version of the Ren'Py SDK made available at that time. At the time of writing, this means that AliceOS is building against Ren'Py SDK v**7.3.5**. If you are unsure of what version AliceOS is built with, check the [GitHub Actions page](https://github.com/projectalicedev/aliceos/actions) and click on "Build AliceOS Archive".
    
    It is recommend that you make sure that your version of Ren'Py is up to date to ensure compatibility with AliceOS.
    
### Usage with DDLC Mods
If you plan to use AliceOS in a mod for _Doki Doki Literature Club!_, you must make sure that the base system version that you use is built against Ren'Py **6.99.12.4** to maintain compatibility.

The release ZIP file is generally noted as `AliceOS-x.x.x-_6.99.12.4-ASBaseSystem.zip`.

## Building from source code

Alternatively, you can build `AliceOSBaseSystem.rpa` yourself with the customization you need. This may also be helpful in building AliceOS for your specific Ren'Py version, if necessary.

1. Download the source code for the particular release you'd like and open Ren'Py Launcher.
2. Select the AliceOS source code and click "Build Distributions".
3. Uncheck the distribution options and check "Alice OS Base System Distributable".
4. Click "Build".

Your resulting ZIP file will be located in `AliceOS-x.x.x-dists`, and you can follow the instructions from **Downloading the base system** to finalize installation.
