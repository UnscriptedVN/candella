# Candella

Candella is a fork of the [AliceOS framework][aliceos], a Ren'Py framework that provides an operating environment to visual novels. This operating environment includes utilities, classes, and other code that lets developers and players write and use apps designed for the system.

!!! warning "Prerelease Notice"
    Candella is in a pre-release state and my change over time. This documentation tries to reflect the most current pre-release version of Candella.

## What makes Candella different?

- **Release compatibility**: Candella's release cycle syncs up with feature releases of Unscripted and the Ren'Py SDK, respectively.
- **Responsive feedback**: AliceOS follows a release schedule and doesn't update as quickly with bug fixes or improvements, Candella gets feedback from the public as well as playtesters in the [Unscripted Playtesting Program][uvn-beta].
- **Targeted for Unscripted**: Candella will add new features and improvements that will be helpful for Unscripted, such as native support for the NadiaVM language.
- **Simplified app development**: Candella's application framework extensions make it easier to develop apps quickly without fiddling through delegate calls.

## Included packages

### Frameworks
- **Observable**: Add observable features to services, apps, and other classes.
- **Multiuser**: Add multi-user support with custom configuration files.
### Core Services
- **Caberto Shell**: A Lomiri-inspired desktop environment with support for multiple users, custom wallpapers, a launcher, and more.
- **Accounts**: Manage different users on a Candella system with ease.
### Apps
- **Glossary**: Look up words that you may not be familiar with as you play through the game.

[aliceos]: https://aliceos.app
[uvn-beta]: https://beta.unscriptedvn.dev
