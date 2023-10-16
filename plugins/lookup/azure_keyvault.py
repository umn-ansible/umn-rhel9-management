# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
  name: Azure Keyvault Lookup
  author: Ian Whitney <whit0694@umn.edu>
  version_added: "0.1"  # same as collection version
  short_description: Retrieves a secret from Azure Key Vault
  description:
    - Follows https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#first-case-access-token-request-with-a-shared-secret
    - This lookup returns the token from Azure Key Vault for UMN Tenants
    - You need to define 3 environment variables for this to work
        - AZURE_SP_CLIENT_ID
        - AZURE_SP_CLIENT_SECRET
        - AZURE_AKV_VAULT_URL
    - You should be able to retrieve all of these from your Key Vault in Azure
    - Do not include the `https://` part of in AZURE_AKV_VAULT_URL.
        - i.e., myvault.vault.azure.net
"""
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
import requests
import os
import urllib.parse

display = Display()

class LookupModule(LookupBase):

    _URL_ = "https://login.microsoftonline.com/c7e9abb7-1aa0-47d4-9ff4-49c649b768fd/oauth2/token"
    
    _AUTH_HEADERS_ = {
                "Content-Type": "application/x-www-form-urlencoded"
                }

    def run(self, terms, variables=None, **kwargs):
      AUTH_BODY = urllib.parse.urlencode({
          "grant_type": "client_credentials",
          "client_id": variables.get("AZURE_SP_CLIENT_ID"),
          "client_secret": variables.get("AZURE_SP_CLIENT_SECRET"),
          "resource": "https://vault.azure.net"
          })
      print(AUTH_BODY)
      VAULT_URL = variables.get("AZURE_AKV_VAULT_URL")
      print(AUTH_URL)
      try:
        res = requests.post(self._URL_, data=AUTH_BODY, headers=self._AUTH_HEADERS_)
        res.raise_for_status()
        lookup_headers = {"Authorization": "Bearer {}".format(res.json()['access_token'])}
      except requests.exceptions.HTTPError as e:
        raise AnsibleError('There was an error getting a token. The lookup API returned %s', res.status_code)
      except Exception as e:
        raise AnsibleError('There was an error %s', e)
      
      ret = []

      for term in terms:
          try:
            url = "https://{}/secrets/{}/?api-version=7.2".format(VAULT_URL, term)
            res = requests.get(url,headers=lookup_headers)
            res.raise_for_status()
            ret.append(res.json()["value"])

          except requests.exceptions.HTTPError as e:
            raise AnsibleError('There was an error getting the credential. The lookup API returned %s', res.status_code)
          except Exception as e:
            raise AnsibleError('There was an error %s', e)

      return ret
