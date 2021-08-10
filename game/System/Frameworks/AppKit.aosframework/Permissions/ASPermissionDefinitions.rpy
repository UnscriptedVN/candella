#
# ASPermissionDefinitions.rpy
# Candella
#
# Created by Marquis Kurt on 1/14/21.
# Copyright © 2019-2021 ProjectAliceDev. All rights reserved.
#

init offset = -1000

# MARK: OS permissions definitions

define AS_REQUIRES_NOTIFICATIONKIT = "REQ_NOTIFICATIONKIT"
define AS_REQUIRES_FULL_DISK_ACCESS = "REQ_FULL_DISK"
define AS_REQUIRES_SYSTEM_EVENTS = "REQ_SYSTEM_EVENTS"


# MARK: OS permissions strings

define AS_REQUIRE_NOTIFKIT_NAME = _("Send Notifications")
define AS_REQUIRE_NOTIFKIT_DESC = _("Notifications may include banners, alerts, and sounds. These can be configured in App Manager.")
define AS_REQUIRE_FDA_NAME = _("Access Your Files")
define AS_REQUIRE_FDA_DESC = _("File access may include your Home directory and your Candella installation. This can be configured in App Manager.")
define AS_REQUIRE_SYSEV_NAME = _("Control Candella Settings")
define AS_REQUIRE_SYSEV_DESC = _("Settings access may include accessibility settings, system events, and preferences. This can be configured in App Manager.")

# MARK: OS permissions enumerations

define AS_REQUIRE_PERMS_NAME = {
    AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_NAME,
    AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_NAME,
    AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_NAME
}

define AS_REQUIRE_PERMS_DESC = {
    AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRE_NOTIFKIT_DESC,
    AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRE_FDA_DESC,
    AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRE_SYSEV_DESC
}