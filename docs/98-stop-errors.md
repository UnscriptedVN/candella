# Common Stop Errors

If Candella encounters an issue that prompts restarting the game (or forcefully quitting it), a Stop error will be displayed on screen. These Stop error screens will display a code that can be used to identify the problem and look for possible solutions.

## `REQUISITE_FRAMEWORK_MISSING`

An app, core service, or framework is requiring a framework that doesn't exist on the system, or it cannot detect the framework it's looking for.

### Common factors that produce this error

- An app, core service, or framework has a misspelling in the framework name in the `requisites` field of the project's manifest.
- The framework the app, core service, or framework is looking for isn't installed in the distribution of Candella.

### Possible solutions

- Check the `requisites` field in the manifest.json file of the project.
- Check that the framework exists in the default framework directory (typically `System/Frameworks/`).
- Reinstall the distribution.

## `MISSING_OOBE_SERVICE`

A core service that provides an out-of-box experience or setup assistant could not be found. This usually occurs when the Roland Boot Manager attempts to run a setup assistant and cannot detect one.

### Common factors that produce this error

- Either the AliceOS Setup Assistant or Thorax core service is missing.

### Possible solutions

- Reinstall the distribution.
