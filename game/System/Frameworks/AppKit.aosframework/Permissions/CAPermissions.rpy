#
# CAPermissions.rpy
# Candella
#
# Created by Marquis Kurt on 1/14/21.
# Copyright © 2021 ProjectAliceDev. All rights reserved.
#

init offset = -1000

init python:
    class CAPermission():
        """A data class that represents a permission for a Candella application."""
        key = "DEFAULT_PERM"
        name = "Default Permission"
        description = "A default permission."
        default_state = False

        def __init__(self, key, name, description, default=False):
            self.key = key
            self.name = name
            self.description = description
            self.default = default

        def __eq__(self, other):
            return isistance(other, CAPermission) and self.key == other.key

        def __ne__(self, other):
            return not self.__eq__(other)

    # This dictionary contains the current system permissions, including the default AliceOS permissions. Apps that
    # use CAApplication instead of ASAppRepresentative can leverage these permission objects by specifying the
    # permissions needed for the app in the 'permissions' field of the app manifest.

    CA_PERMISSIONS = {
        "notifications": CAPermission(
            "REQ_NOTIFICATIONKIT",
            "Send Notifications",
            "Notifications may include banners, alerts, and sounds. These can be configured in App Manager."
        ),
        "file_system": CAPermission(
            "REQ_FULL_DISK",
            "Access The File System",
            "File access includes your user configuration file and may include other files present in Candella. This"
                + " can be configured in App Manager."
        ),
        "system_events": CAPermission(
            "REQ_SYSTEM_EVENTS",
            "Control System Events",
            "System events include login, shutdown, or user switching. This can be configured in App Manager."
        ),
        "manage_users": CAPermission(
            "REQ_USERS_MANAGEMENT",
            "Manage Users",
            "User management includes adding, modifying, and removing users. This can be configured in App Manager."
        ),
        "virtual_platform": CAPermission(
            "REQ_METEORVM",
            "Run Apps in a Virtual Environment",
            "This app runs additional code in the Meteor VM platform. This can be configured in App Manager."
        ),

    }
