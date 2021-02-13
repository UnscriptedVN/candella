from candella_sdk import sdk
import os


def test_all_apps_validate():
    for application in os.listdir(os.path.join("game", "System", "Applications")):
        if not application.endswith(".aosapp"):
            continue
        validation, _ = sdk.validate(os.path.join(
            "game", "System", "Applications", application))
        assert validation
