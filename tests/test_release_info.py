import pytest
import json


def test_release_manifest():
    """Test that the release info file in the System folder has the correct keys loaded."""
    manifest = {}
    required_keys = ["name", "version", "build_id", "channel", "codename"]

    with open("game/System/release_info.json", 'r') as manifest_file:
        manifest = json.load(manifest_file)
    
    assert "distribution" in manifest and sorted(list(manifest["distribution"].keys())) == sorted(required_keys)