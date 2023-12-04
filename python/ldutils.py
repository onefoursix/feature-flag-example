#!/usr/bin/env python3

"""
Utils for working with LaunchDarkly

Assumes the LaunchDarkly SDK API Key has been set in the environment variable LAUNCH_DARKLY_SDK_API_KEY

For example: $ export LAUNCH_DARKLY_SDK_API_KEY="sdk-1a1a1a1a1a-1a1a-1a1a-1a1a-1a1a1a1a1a1a"
"""

import ldclient
from ldclient.config import Config
import os


# Get the LaunchDarkly API Key from the environment
def get_ld_api_key():
    ld_api_key = os.getenv('LAUNCH_DARKLY_SDK_API_KEY')
    if ld_api_key is None or len(ld_api_key) == 0:
        print('\nError: LaunchDarkly SDK API Key is not set in the environment.')
        print('Execute the command \'$ export LAUNCH_DARKLY_SDK_API_KEY="<your API key>"\' and run the app again')
        print('For example: $ export LAUNCH_DARKLY_SDK_API_KEY="sdk-1a1a1a1a1a-1a1a-1a1a-1a1a-1a1a1a1a1a1a"\n')
        return None
    return ld_api_key


# Init the LaunchDarkly API
def ldclient_init():
    ldclient.set_config(Config(get_ld_api_key()))
    if ldclient.get().is_initialized():
        print('LaunchDarkly SDK successfully initialized!')
    else:
        raise Exception('LaunchDarkly SDK failed to initialize.')
