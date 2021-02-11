# 
# version_inject.py
# Candella
# 
# Created by Marquis Kurt on 02/10/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
#!/bin/env python3

from datetime import datetime
import os
import json
from typing import Dict

def stamp_channel(build_id: str, lsb_release: Dict, id_hashed: bool = False):
    if "beta" in build_id:
        lsb_release["distribution"]["channel"] = "beta"
    elif "rc" in build_id and not id_hashed:
        lsb_release["distribution"]["channel"] = "candidate"
    else:
        lsb_release["distribution"]["channel"] = "stable"

current = datetime.now()

# Get the release data file from the System folder.
with open(os.path.join("game", "System", "release_info.json"), 'r') as release_data:
    lsb_release = json.load(release_data)

# Update the version to follow Ubuntu-styled releases (YY.MM).
lsb_release["distribution"]["version"] = __ver = f"{str(current.year)[2:]}.{current.month:02d}"
print(f"Release version dated : {__ver}")

# Replace the build ID string with either the tag, commit hash, or date the product was built.
if "tag" in os.environ and os.environ["tag"]:
    tag = os.environ["tag"]
    print(f"Tag {tag} found. Using tag as Build ID.")
    tag = tag.replace("refs/tags", "")
    lsb_release["distribution"]["build_id"] = os.environ["tag"]

    # Update the channel based on the tag information.
    stamp_channel(tag, lsb_release)
    __chan = lsb_release["distribution"]["channel"]
    print(f"Channel for distribution set to: {__chan}")

elif "commit" in os.environ and os.environ["commit"]:
    print("Commit hash found. Using commit hash as Build ID.")
    lsb_release["distribution"]["build_id"] = os.environ["commit"][:7]
else:
    print("No tags or commits found. Using date/time as Build ID.")
    lsb_release["distribution"]["build_id"] = \
        f"{current.year}{current.month:02d}{current.day}-{current.hour}{current.minute}{current.second}"

# Record the build date in the release info file, since Candella and other derivatives won't read it.
lsb_release["build_date"] = current.isoformat()

# Save the changes back to the file.
with open("game/System/release_info.json", "w+") as release_data_writable:
    json.dump(lsb_release, release_data_writable, indent=4)
