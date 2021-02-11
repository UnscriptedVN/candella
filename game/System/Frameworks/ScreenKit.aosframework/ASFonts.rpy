#
# ASFonts.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init:
    style ASSystemRegularFont is default:
        font get_font("Interface")
            outlines []

    style ASSystemBoldFont is default:
        font get_font("Interface", variant="Bold")
            outlines []

    style ASSystemMediumFont is default:
        font get_font("Interface", variant="Medium")
        outlines []

    style ASSystemBlackFont is default:
        font get_font("Interface", variant="Black")
        outlines []

    style ASSystemItalicFont is default:
        font get_font("Interface", variant="Italic")
        outlines []

    style ASSystemThinFont is default:
        font get_font("Interface", variant="Thin")
        outlines []

    style ASSystemMonoFont is default:
        font get_font("Interface", variant="Mono")
        outlines []
