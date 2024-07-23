# UMN RHEL9 Management Collection

This collection contains tools to assist with managing RHEL9 hosts via Tower. 

## What's in here

### Azure Secrets Lookup Plugin

Retrieves secrets from Azure Key Vault. 

Populate these secrets to enable lookup plugin:
- AZURE_SP_CLIENT_ID
- AZURE_SP_CLIENT_SECRET
- AZURE_AKV_VAULT_URL

Do not include the `https://` part of in AZURE_AKV_VAULT_URL.

Once you've populated those values, you can use the plugin anywhere in your playbook using the lookup command: `lookup('umn_community.umn_rhel9_management.azure_keyvault', 'name-of-your-secret')`

### User Management Role

The documentation for the user management role is available in a [separate repo](http://github.com/umn-ansible/umn_user_management_role). To use the role via this collection, use the full collection name:

```
roles:
    - umn_community.umn_rhel9_management.umn_user_management_role
```