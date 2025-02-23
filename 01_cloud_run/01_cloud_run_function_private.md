
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
