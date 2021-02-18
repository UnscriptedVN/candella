#
# CADeprecated.py
# Candella
#
# Created by Marquis Kurt on 02/17/21.
# Copyright © 2021 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -50
init python in CADeprecated:
    from functools import wraps
    from store import clog
    import logging
    import warnings

    def deprecated(version, renamed=None, reason=None):
        """Mark a function or method as deprecated.

        This is typically used as a decorator on existing methods or functions to mark that they are deprecated.

        Args:
            version (str): The version that this method or function is deprecated in.
            renamed (str): The renamed function to use instead.
            reason (str): The reason for the deprecation.
        """
        def __deprecated(method):
            if renamed:
                dep_msg = method.__name__ + " has been renamed in version " + version + " to: " + renamed
            elif reason:
                dep_msg = method.__name__ + " has been deprecated in version " + version + ": " + reason
            else:
                dep_msg = method.__name__ + " has been deprecated in version " + version

            @wraps(method)
            def __wrapped_call(*args, **kwargs):
                warnings.warn(dep_msg)
                clog.warn(dep_msg)
                method(*args, **kwargs)

            return __wrapped_call

        return __deprecated
