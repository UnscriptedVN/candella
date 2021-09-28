#
# logger.rpy
# Candella - Logger
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init offset = -5000

# The following creates a basic logger that will be saved in the user's save directory of the game.
# This log is used to log Candella events instead of directing output to the console.

init python:
    import logging
    
    clog = logging.getLogger('dev.unscriptedvn.candella')
    clog.setLevel(logging.DEBUG)
    
    _clog_fhandler = logging.FileHandler(config.savedir+"/candella.log")
    _clog_fhandler.setLevel(logging.DEBUG)
    
    _clog_chandler = logging.StreamHandler()
    _clog_chandler.setLevel(logging.ERROR)
    
    clog_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    _clog_fhandler.setFormatter(clog_format)
    _clog_chandler.setFormatter(clog_format)
    
    clog.addHandler(_clog_fhandler)
    clog.addHandler(_clog_chandler)
    
    clog.debug("Opened debug file and started a new session.")