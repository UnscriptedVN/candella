#
# Messages.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:
    class ASMessages(CAApplication):
        def __init__(self):
            CAApplication.__init__(self, AS_DEFAULT_APP_DIR + "Messages.aosapp/")

        def receiveMessage(self, fromPerson, message):
            return self.applicationWillRequestNotification(message=fromPerson, withDetails=message)

        def applicationShouldRequestNotification(self):
            return True

        def applicationWillLaunch(self):
            banner = CANotificationBanner(
                _("Messages app functionality not implemented."),
                _("You will still be able to receive message notifications from characters in-game.")
            )
            banner.callback_text = _("Dismiss")
            self.send_banner("automatic", banner=banner)

    messages = ASMessages()
