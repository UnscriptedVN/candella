from candella_sdk import sdk
import os


def test_all_services_validate():
    for service in os.listdir(os.path.join("game", "System", "CoreServices")):
        if not service.endswith(".aoscservice"):
            continue
        validation, reason = sdk.validate(os.path.join(
            "game", "System", "CoreServices", service))
        print(f"{service}: {reason}")
        assert validation
