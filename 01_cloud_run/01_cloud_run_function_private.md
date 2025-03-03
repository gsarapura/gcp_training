
# Cloud Run Function 
In case it does not allow unauhtneticated access, it must be access via IAM roles:
```bash
curl -X POST https://test-delete-later-37120935558.us-central1.run.app \
     -H "Authorization: bearer $(gcloud auth print-identity-token)" \
     -H "Content-Type: application/json" \
     -d '{
        "name": "Developer"
        }'
```

# Authenticate for invocation

https://cloud.google.com/functions/docs/securing/authenticating#id-tokens


# Generate tokens manually
https://cloud.google.com/functions/docs/securing/authenticating#generate_tokens_manually

## Exchange a self-signed JWT for a Google-signed ID token
https://cloud.google.com/functions/docs/securing/authenticating#exchange_a_self-signed_jwt_for_a_google-signed_id_token