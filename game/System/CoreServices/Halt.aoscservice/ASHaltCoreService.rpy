#
# ASHaltCoreService.rpy
# Candella
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init 5 python:
    import os
    import logging

    class ASHaltCoreService(CACoreService):

        def __init__(self):
            CACoreService.__init__(self, AS_CORESERVICES_DIR + "Halt.aoscservice/")

        def _write_halt(self, code=""):
            template = """\
Candella has encountered an error it couldn't handle and has been shut down to prevent further damage.
You can search the error in the Error Database at https://errordb.aliceos.app for more information.

This message is usually displayed if Candella could not restart the system for a reason. You can read
the logs at the listed directory below to follow up on what led to the Stop error.

Log file: %s

Stop Code: %s
Candella Version: %s
Candella Version Build: %s
Ren'Py Version: %s
Host Operating System: %s
            """ % (
                os.path.join(config.savedir, "candella.log"),
                code,
                AS_SYS_INFO["VERSION"],
                AS_SYS_INFO["BUILD_ID"],
                renpy.version(),
                renpy.platform
            )
            try:
                with open("candella_stop.txt", "w+") as error_file:
                    error_file.write(template)
                renpy.exports.launch_editor([ "candella_stop.txt" ], 1, transient=1)
            except:
                print(template)

        def halt(self, code="", write=False):
            clog.error("Received Stop error code: %s. Halting and restarting.", code)
            try:
                if write:
                    raise Exception
                renpy.call_screen("ASHaltMessage", error=code)
            except renpy.game.UtterRestartException: # If we're restarting, don't write the file.
                return
            except Exception as exception:
                clog.error("Failed to display Stop screen. Reason: %s", exception)
                self._write_halt(code)
                clog.info("Wrote stop file to candella_stop.txt.")
                renpy.quit()


    ASHalt = ASHaltCoreService()
