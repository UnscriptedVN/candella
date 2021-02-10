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

lsb_release = {}

with open("game/System/release_info.json", 'r') as release_data:
    lsb_release = json.load(release_data)

if os.environ["tag"]:
    tag = os.environ["tag"]
    print(f"Tag {tag} found. Using tag as Build ID.")
    tag = tag.replace("refs/tags", "")
    lsb_release["distribution"]["build_id"] = os.environ["tag"]
elif os.environ["commit"]:
    print("Commit hash found. Using commit hash as Build ID.")
    lsb_release["distribution"]["build_id"] = os.environ["commit"][:7]
else:
    print("No tags or commits found. Using date/time as Build ID.")
    current = datetime.now()
    lsb_release["distribution"]["build_id"] = f"{current.year}{current.month}{current.day}"

with open("game/System/release_info.json", "w+") as release_data_writable:
    json.dump(lsb_release, release_data_writable, indent=4)