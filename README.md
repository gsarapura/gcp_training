# gcp_training

# GCloud CLI
- [Install](https://cloud.google.com/sdk/docs/install)
```bash
# First time
gcloud init

# Authorize with a user account without setting up a configuration.
gcloud auth login
# Authorize with a service account instead of a user account. Useful for authorizing non-interactively and without a web browser.
gcloud auth activate-service-account

# List
gcloud config list
gcloud auth list

# Remove 
gcloud auth revoke

# Switch different accounts
gcloud config set account $ACCOUNT

```