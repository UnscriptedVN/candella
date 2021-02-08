# Caberto Shell

The default desktop shell for Candella is **Caberto**. Caberto's interface is mainly inspired from the [Lomiri][lomiri] desktop environment and comes with per-user customizations.

Caberto is currently in a pre-release state and the documentation here may change as the project evolves.

![Default Caberto Shell desktop](./images/caberto/default.png)

## Using Caberto Shell

There are two major components to Caberto Shell: the top bar and the launcher on the left-hand side of the screen. In the top bar, you can view the currently-running application's name, the current user, the time, and a few status indicators for settings and exiting the desktop. The launcher on the left displays favorite apps and provides the main entry point to access all apps.

![Caberto Shell drawer](./images/caberto/drawer.png)

### Customizing the desktop

Click on the gear in the top bar to open the Settings pane for Caberto Shell. Currently, the only setting available in this panel is the wallpaper selection.

![Caberto Shell settings](./images/caberto/settings.png)

### Switching users

To switch the current user that's logged in to the system, click on the current user's name in the top bar and then select the user to switch to.

### Pinning apps to the launcher

The App Manager app provides access to pinning apps. Open the App Manager app, click on the app you want to pin from the left side, and then check the box labeled "Pin to launcher", next to the launch button.

![App Manager](./images/caberto/appman.png)

## Available methods for developers

Caberto Shell provides some static methods that developers can use to get information present in Caberto Shell easily:

- `CabertoShell.get_all_applications()` returns all of the classes and instanced apps available to Candella.
- `CabertoShell.wallpapers()` returns a list containing the names of the wallpapers available to Caberto Shell.
- `CabertoShell.current_time()` returns a string that represents the current time on the system.

[lomiri]: https://lomiri.com