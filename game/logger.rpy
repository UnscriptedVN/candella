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
    
    logging.basicConfig(
        filename=config.savedir+"/candella.log",
        encoding='utf-8',
        format="%(asctime)s [%(levelname)s] %(message)s",
        level=logging.DEBUG
    )
    logging.debug("Opened debug file and started a new session.")