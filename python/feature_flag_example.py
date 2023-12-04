#!/usr/bin/env python3

"""
Example implementation of the use of a LaunchDarkly feature flag

The 'get_ui(user)' method will return either the new UI or the old UI
based on the 'use_new_ui' feature flag and targeting rules for the given user
"""
import ldclient
from ldclient import Context
import ldutils
import sys


class FeatureFlagExample:
    def __init__(self):
        try:
            # Init LaunchDarkly
            ldutils.ldclient_init()
        except Exception as e:
            # Exit on error in LaunchDarkly init
            print(str(e))
            sys.exit(1)

    #  Return either the old UI or the new UI for the user
    #  based on the 'use_new_ui' feature flag and targeting rules
    def get_ui(self, user: str):

        # Create a LaunchDarkly context for the user
        context = Context.builder(user).name(user).build()

        # Get the 'use_new_ui' feature flag
        use_new_ui_flag = ldclient.get().variation('use_new_ui', context, False)

        print("Feature flag 'use_new_ui' is {} for {}".format(use_new_ui_flag, user))

        if use_new_ui_flag:
            # Use the new UI (mocked up as a png file)
            return '../images/new-ui.png'
        else:
            # Use the old UI (mocked up as a png file)
            return '../images/old-ui.png'
