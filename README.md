# UMN Azure Management Collection

This collection contains useful integrations to work with Azure from Ansible. 

## What's in here

### Azure Secrets Lookup Plugin

Retrieves secrets from Azure Key Vault. 

Populate these secrets to enable lookup plugin:
- AZURE_SP_CLIENT_ID
- AZURE_SP_CLIENT_SECRET
- AZURE_AKV_VAULT_URL

Do not include the `https://` part of in AZURE_AKV_VAULT_URL.