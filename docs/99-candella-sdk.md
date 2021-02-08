# Candella SDK

The Candella SDK application is a command-line utility that aims to make Candella development easier. The SDK provides utilities to create apps, core services, and frameworks automagically with an interactive tool.

## Quickstart: Install from PyPI

To install the Candella SDK, you can run the following command via PyPI:

```
pip install candella-sdk
```

!!! warning
    The Candella is in a pre-release state and isn't available in PyPI yet. You will need to build the project from source to use the SDK.

## Build the SDK from source

You will need the following dependencies installed:

- Python 3.8 or greater
- Poetry 1.1.4 or greater

Clone the project from GitHub and run the following commands in the root of the project:

```
poetry install
poetry build
```

## Creating projects

Currently, the Candella SDK lets you create three different kinds of projects: applications, core services, and frameworks. To create any of these projects, run `candella-sdk --create` and specify the `--type` argument:

- `--type application` to create an application.
- `--type service` to create a core service.
- `--type framework` to create a framework.

!!! note
    If you choose an open-source license, you will need to supply the LICENSE file with your app. This may be updated in a future release of the SDK.