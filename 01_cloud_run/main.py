import json
import time
import jwt
import requests
from google.auth import crypt
from google.auth.transport.requests import Request

# Load the service account private key
with open('pco-qa-199c54d6370c.json') as f:
    private_key_info = json.load(f)

# Extract private key and client email
private_key = private_key_info['private_key']
client_email = private_key_info['client_email']

# Set the target audience (URL of the Cloud Function you want to invoke)
# target_audience = "https://REGION-PROJECT_ID.cloudfunctions.net/YOUR_FUNCTION_NAME"
target_audience = "https://test-delete-later-339009847298.us-central1.run.app"

# Prepare the JWT header
header = {
    "alg": "RS256",
    "typ": "JWT"
}

# Prepare the JWT payload
payload = {
    "iss": client_email,           # Issuer (service account email)
    "sub": client_email,           # Subject (service account email)
    "aud": "https://www.googleapis.com/oauth2/v4/token",  # Audience (Google OAuth endpoint)
    "exp": int(time.time()) + 3600,  # Expiration time (1 hour)
    "iat": int(time.time()),        # Issued at time
    "target_audience": target_audience  # Audience for the Cloud Function
}

# Sign the JWT with the service account private key
jwt_token = jwt.encode(payload, private_key, algorithm='RS256', headers=header)
print(f"JWT: {jwt_token}")

# Exchange the JWT for a Google-signed ID token
token_url = "https://www.googleapis.com/oauth2/v4/token"
data = {
    "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "assertion": jwt_token
}

response = requests.post(token_url, data=data)

if response.status_code == 200:
    id_token = response.json().get("id_token")
    print(f"ID Token: {id_token}")
else:
    print(f"Error exchanging JWT for ID token: {response.status_code}, {response.text}")
    exit(1)

# Invoke the Cloud Function using the Google-signed ID token
# function_url = "https://REGION-PROJECT_ID.cloudfunctions.net/YOUR_FUNCTION_NAME"
function_url = "https://test-delete-later-339009847298.us-central1.run.app"
headers = {
    "Authorization": f"Bearer {id_token}"
}

response = requests.get(function_url, headers=headers)  # Use POST if needed

if response.status_code == 200:
    print(f"Cloud Function Response: {response.text}")
else:
    print(f"Error invoking Cloud Function: {response.status_code}, {response.text}")
