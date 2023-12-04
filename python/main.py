#!/usr/bin/env python3

"""
Example service to demonstrate the use of a LaunchDarkly feature flag and targeting rule.
See the README.md for details, prerequisites, and test cases
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

        # See if a user arg is present
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
