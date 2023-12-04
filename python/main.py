#!/usr/bin/env python3

"""
Example service to demonstrate the use of a LaunchDarkly feature flag and targeting rule.

Prerequisites

- A Python 3.8+ environment

- Flask -- see https://pypi.org/project/Flask/) - A Python web application framework (tested with v3.0.0)

- LaunchDarkly SDK for Python (tested with v9.0.1)

- This example depends on a boolean feature flag named use_new_ui

Requires the LaunchDarkly SDK API Key to be set in the environment variable LAUNCH_DARKLY_SDK_API_KEY

For example: $ export LAUNCH_DARKLY_SDK_API_KEY="sdk-1a1a1a1a1a-1a1a-1a1a-1a1a-1a1a1a1a1a1a"

Edit the host and port variable values in this file if you want the service to listen on a particular hostname or port.
The default is to listen on all interfaces on port 8888

Launch the example like this:

- Clone this project

- Change to the project's python directory

- Set and export the environment variable LAUNCH_DARKLY_SDK_API_KEY as described above

- Execute the command $ python3 main.py

- Point your browser to http://<host>:8888
  For example, if running the example on your local machine, use http://localhost:8888

See the README.md for details and test cases

"""

from flask import Flask, request, send_file
from feature_flag_example import FeatureFlagExample

# Host and port the service will listen on
host = '0.0.0.0'
port = 8888

app = Flask(__name__)


# Handle a request to the Service
@app.route('/', methods=['GET'])
def handle_request():
    try:

        # Parse the query string
        request_args = request.args.to_dict()

        # See is a user arg is present
        if 'user' in request_args.keys():
            user = request_args['user']
        else:
            user = 'anonymous'

        # Get either the old UI or the new UI for the user
        # based on the 'use_new_ui' feature flag and targeting rules
        ui = feature_flag_example.get_ui(user)

        # return the response (with the UI mocked as a png)
        return send_file(ui, mimetype='image/png')

    except Exception as e:
        return {"status": "There was an error: " + str(e)}


if __name__ == '__main__':
    # Init the example and the LaunchDarkly SDK
    feature_flag_example = FeatureFlagExample()

    # Start the service
    app.run(debug=True, host=host, port=port)
