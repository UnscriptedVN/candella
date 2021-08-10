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
    from store import clog, AS_SYS_INFO
    import logging
    import warnings

    __OS_VERSIONS = ["*", "apple-cinnamon", "bahama"]

    class CAMinimumVersionNotSupportedError(Exception):
        """The current OS version doesn't meet the minimum requirements."""

    def __version_meets_minimum_requirements(version, minimum_version):
        minimum_idx = __OS_VERSIONS.index(minimum_version)
        current_idx = __OS_VERSIONS.index(version)
        return current_idx >= minimum_idx

    def available(minimum_codename, introduced="apple-cinnamon", deprecated=None, message=None):
        """Restrict usage of a function to specific OS versions.

        This can be used to determine if a method or function should be marked as deprecated, or if a function is only
            available on a specific minimum OS version.
        
        Args:
            minimum_codename (str): The minimum OS version that this function supports. To support all, use '*'.
            introduced (str): The OS version that this function was introduced. Defaults to apple-cinnamon.
            deprecated (str): The OS version that this function was deprecated. Defaults to None.
            message (str): A message used to mark why something is deprecated or introduced. Defaults to None.
        """
        def __available(method):
            deprecated_msg = "%s has been deprecated in version %s: %s" % (method.__name__, deprecated, message)
            minimum_ver_msg = "%s requires OS version %s or greater. (%s)" % (
                method.__name__, minimum_codename, AS_SYS_INFO["COMMON_NAME"])

            @wraps(method)
            def __wrapped_call(*args, **kwargs):
                if not __version_meets_minimum_requirements(AS_SYS_INFO["COMMON_NAME"], minimum_codename):
                    raise CAMinimumVersionNotSupportedError(minimum_ver_msg)
                if deprecated and __version_meets_minimum_requirements(current, deprecated):
                    warnings.warn(deprecated_msg)
                    clog.warn(deprecated_msg)

                if method.__doc__ is None:
                    method.__doc__ = method.__name__ + " Documentation\n"
                
                if introduced:
                    method.__doc__ += "\nCandella Verison Introduced: %s" % (introduced)
                if deprecated:
                    method.__doc__ += "\nCandella Version Deprecated: %s" % (deprecated)
                    if message:
                        method.__doc__ += " (%s)" % (message)

                return method(*args, **kwargs)
            return __wrapped_call
        return __available

    @available('*', introduced="apple-cinnamon", deprecated="bahama", message="Use @available decorator instead.")
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
                return method(*args, **kwargs)

            return __wrapped_call

        return __deprecated
