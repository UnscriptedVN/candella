from candella_sdk import sdk
import os
import pytest


def test_all_frameworks_validate():
    for framework in os.listdir(os.path.join("game", "System", "Frameworks")):
        if not framework.endswith(".aosframework"):
            continue
        validation, _ = sdk.validate(os.path.join(
            "game", "System", "Frameworks", framework))
        assert validation
