# Writing a Candella app

> :warning: This documentation is incomplete and may change over time.

Candella includes support for writing miniature apps that work within the Candella system. These apps sit on top of the AppKit framework for AliceOS (not to be confused with Apple's AppKit).

## Creating an app

### The manifest file

The manifest file contains information about your app, as well as what the app needs from Candella to run. The manifest file is located in the root of the app as `manifest.json`. Candella will automatically fill in the information of the app for you as the Ren'Py project initializes.

- `name`: A short name of your app. This can also be used as the command name.
- `productName`: A human-readable version of the app name.
- `id`: An identifier for the app. It is recommended to use reverse domain notation.
- `author`: The author of the app. It is recommended to use the `Name <name@email.server>` format.
- `version`: The current version of the app.
- `description`: A summary of what your app does.
- `license`: The license your app falls under as an SPDX expression.
- `permissions`: A list of strings containing what permissions your app requires:
  - `file_system`: Requires access to the Candella "file system"
  - `notifications`: Requires access to NotificationKit to send notifications
  - `system_events`: Requires access to System Events
  - `virtual_platform`: Requires access to the MeteorVM platform

The following is an example manifest:

```json
{
    "name": "textedit",
    "productName": "Text Editor",
    "id": "com.appleseed.text-editor",
    "author": "John Appleseed <john@appleseed.email>",
    "version": "12.0.0",
    "description": "A simple text editor for Candella.",
    "license": "GPL-3.0",
    "requires": ["file_system"]
}
```

## Sending app signals

Apps can send information to other services and even other apps. Candella apps adopt the Observable framework, which allows for signal emission.

To emit a signal from your app, use the `emit_signal` method, followed by what you want to send.

For instance, if you have an arcade shooter game `ArcadeShooter` and wanted to emit a signal to any receivers with an updated score:

```py
class ArcadeShooter(CAApplication):
    # ...
    def submit_score(self, score=0):
        self.score = score

        # Emit a signal with the updated score.
        # Apps and services that are listening to this
        # signal can access the score with kwargs["score"].
        self.emit_signal("score_submitted", score=score)
```

The following signals are automatically emitted by `CAApplication`:
- `application_launched` (`name=self.get_name()`)
- `application_terminated`
- `banner_sent` (`response=any`)
- `alert_sent` (`response=any`)