# Candella

Candella is a refreshed fork of the [AliceOS](https://aliceos.app) framework for Ren'Py. Candella is primarily targeted for Unscripted, but maintains compatibility with AliceOS APIs for other Ren'Py distributions.

## Differences between AliceOS

- **Release compatibility**: Candella's release cycle syncs up with feature releases of Unscripted and the Ren'Py SDK, respectively.
- **Responsive feedback**: AliceOS follows a release schedule and doesn't update as quickly with bug fixes or improvements, Candella gets feedback from the public as well as playtesters in the [Unscripted Playtesting Program][uvn-beta].
- **Targeted for Unscripted**: Candella will add new features and improvements that will be helpful for Unscripted, such as native support for the NadiaVM language.

## Getting started

### Quick start: Get Candella

Every copy of Unscripted comes with Candella pre-installed. To import this into another Ren'Py project, copy the `aos-base.rpa` file from Unscripted to your Ren'Py project.

Likewise, you can download the latest release from GitHub Releases.

### Build from source

#### Requirements
- Ren'Py SDK v7.4.0 or greater

To build this project, clone the repository and in Ren'Py Launcher, click "Distribute" and select "Candella System Distributable". The resulting file will be in a ZIP archive with AliceOSBaseSystem.rpa.

## License

Candella is licensed under the BSD-2-Clause license per the licensing of the original AliceOS project.

<!-- Links -->
[uvn-beta]: https://beta.unscriptedvn.dev