# Candella SDK

The Candella SDK application is a command-line utility that aims to make Candella development easier. The SDK provides utilities to create apps, core services, and frameworks automagically with an interactive tool.

## Quickstart: Install from PyPI

To install the Candella SDK, you can run the following command via PyPI:

```
pip install candella-sdk
```

!!! warning
    The Candella SDK is in a pre-release state. Features, methods, and APIs may change over time.

## Build the SDK from source

You will need the following dependencies installed:

- Python 3.8 or greater
- Poetry 1.1.4 or greater

Clone the project from GitHub and run the following commands in the root of the project:

```
poetry install
poetry build
```

Then, use `pip install` and point to the resulting wheel file in the `dist` directory.

## Creating projects

Currently, the Candella SDK lets you create three different kinds of projects: applications, core services, and frameworks. To create any of these projects, run `candella-sdk --action create` and specify the `--type` argument:

- `--type app` to create an application.
- `--type service` to create a core service.
- `--type framework` to create a framework.

!!! note
    If you choose an open-source license, you will need to supply the LICENSE file with your app. This may be updated in a future release of the SDK.

## Validating projects

The Candella SDK provides a rudimentary validation system for projects to ensure that apps, core services, and frameworks have proper manifests and the materials needed for the project to run in Candella.

To start validating a project, run `candella-sdk --action validate` and specify the `--project` argument with the path to your project.

Currently, the SDK will check for the following:

- That the project is a valid Candella project
- That the project contains a manifest file
- That the project's manifest file contains the required keys and doesn't include invalid keys
- That the project contains the proper iconset if the project is an app or core service

!!! warning "About project validation"
    Remember that project validation is not a substitution for thorough testing, nor does it guarantee that your project will work correctly with Candella.
    
    Always remember to thoroughly test your projects and how they work in the most recent versions of Candella alongside the most recent versions of the frameworks and core services included.

## Using Candella SDK programmatically

The Candella SDK can be imported as a Python module into a script to automate development or to write tests for validating apps.

Creating a project can be performed by calling `sdk.create` with a single argument that defines the project type:

```py
from candella_sdk import sdk, CandellaProjectType

sdk.create(CandellaProjectType.application)
```

Likewise, a project can be validated programmatically by calling `sdk.validate` and passing in the path to the project to validate. The validation function returns a tuple containing if the project was validated, and the error in question if the validation failed.

```py
from candella_sdk import sdk

validated, error = sdk.validate("path/to/Example.aosapp")
if not validated:
    raise Exception(error)
```