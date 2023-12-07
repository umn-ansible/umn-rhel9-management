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

Once you've populated those values, you can use the plugin anywhere in your playbook using the lookup command: `lookup('umn_community.umn_rhel9_management.azure_keyvault', 'name-of-your-secret')`
