#
# logger.rpy
# Candella - Logger
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -1000

# The following creates a basic logger that will be saved in the user's save directory of the game.
# This log is used to log Candella events instead of directing output to the console.

init python:
    import logging
    
    clog = logging.getLogger('dev.unscriptedvn.candella')
    clog.setLevel(logging.DEBUG)
    
    clog_fhandler = logging.FileHandler(config.savedir+"/candella.log")
    clog_fhandler.setLevel(logging.DEBUG)
    
    clog_chandler = logging.StreamHandler()
    clog_chandler.setLevel(logging.ERROR)
    
    clog_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    clog_fhandler.setFormatter(clog_format)
    clog_chandler.setFormatter(clog_format)
    
    clog.addHandler(clog_fhandler)
    clog.addHandler(clog_chandler)
    
    clog.debug("Opened debug file and started a new session.")