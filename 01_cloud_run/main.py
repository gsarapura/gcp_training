import urllib
import urllib.request
import logging

import google.auth.transport.requests
import google.oauth2.id_token


def make_authorized_get_request(endpoint, audience):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    by authenticating with the ID token obtained from the google-auth client library
    using the specified audience value.
    """

    # Cloud Functions uses your function's URL as the `audience` value
    # audience = https://project-region-projectid.cloudfunctions.net/myFunction
    # For Cloud Functions, `endpoint` and `audience` should be equal

    req = urllib.request.Request(endpoint)
    logging.info("*req value: %s", req)

    auth_req = google.auth.transport.requests.Request()
    logging.info("*auth req value: %s", auth_req)
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)
    logging.info("*id token value: %s", id_token)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    return response.read()


def main():
    endpoint_audience = "https://test-delete-later-37120935558.us-central1.run.app"
    logging.basicConfig(level=logging.DEBUG)
    make_authorized_get_request(endpoint_audience, endpoint_audience)


if __name__ == '__main__':
    main()
