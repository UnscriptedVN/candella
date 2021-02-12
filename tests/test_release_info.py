from os import path
from datetime import datetime as dt
from ..scripts import vi
import re as regex
import json


def __get_manifest():
    with open(path.join("game", "System", "release_info.json"), 'r') as manifest_file:
        return json.load(manifest_file)


def test_release_manifest():
    """Test that the release info file in the System folder has the correct keys loaded."""
    manifest = __get_manifest()
    required_keys = ["name", "version", "build_id", "channel", "codename"]
    
    assert "distribution" in manifest and sorted(list(manifest["distribution"].keys())) == sorted(required_keys)


def test_release_version_matches():
    """Test that the release version information in the version field matches the current runtime."""
    manifest = __get_manifest()
    
    date = manifest["distribution"]["version"]
    current_dt = dt.now()
    assert date == f"{str(current_dt.year)[2:]}.{current_dt.month:02d}"


def test_release_channel_validity():
    """Test that the channel listed in the release info is valid."""
    manifest = __get_manifest()
    assert manifest["distribution"]["channel"] in ["stable", "beta", "candidate", "edge"]


def test_release_codename_validity():
    """Test that the codename in the release field doesn't contain invalid characters."""
    manifest = __get_manifest()
    assert regex.match("^[a-zA-Z_-]*$", manifest["distribution"]["codename"])


def test_release_updater():
    assert vi.update_release_information()
