# Getting started

## Quick start: Get Candella

Unscripted comes bundled with the latest release of Candella and can be copied to any Ren'Py project. In the game's files, copy the 'candella.rpa' archive to your Ren'Py project.

You can additionally download a release from [the Releases page][releases], or you can grab the latest release from [Itch.io][itch].

## Build from source

### Requirements
- [Ren'Py SDK][renpy] v8.0.3 or greater
- Python 3
- Pipenv

!!! warning
    Starting with the Bahama release, Candella builds for Python 3. Make sure you have the appropriate tooling to ensure a successful build.

Clone the repository from GitHub, then run `pipenv install -d` in the root of the project to fetch dependencies for making the project.

To build this project, open the Ren'Py Launcher, click "Distribute" and select "Candella System Distributable". The resulting file will be in a ZIP archive with `candella.rpa`.

### Test-drive features

If you want to test out some of the features without building anything, clone the repository and launch the project from the Ren'Py launcher.


[renpy]: https://renpy.org/latest
[releases]: https://github.com/UnscriptedVN/candella/releases
[itch]: https://marquiskurt.itch.io/candella