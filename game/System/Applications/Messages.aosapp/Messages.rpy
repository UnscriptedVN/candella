#
# Messages.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:
    class ASMessages(ASAppRepresentative):
        bundleName = "Messages"
        bundleId = "dev.unscriptedvn.candella.messages"
        bundleDir = AS_DEFAULT_APP_DIR + "Messages.aosapp/"
        bundleAuthor = "Project Alice and Unscripted Team"
        bundleVersion = "2.0.0"
        bundleDescription = """\
            Send and receive messages from your favorite characters in-game.
        """

        requires = {
            AS_REQUIRES_NOTIFICATIONKIT
        }

        def receiveMessage(self, fromPerson, message):
            return self.applicationWillRequestNotification(message=fromPerson, withDetails=message)

        def applicationShouldRequestNotification(self):
            return True

        def applicationWillLaunch(self):
            self.applicationWillRequestBasicAlert("Messages Not Ready", "You'll still be able to receive notifications from characters in-game, but you won't be able to send any.")
            return

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Messages.aosapp/")

    messages = ASMessages()
