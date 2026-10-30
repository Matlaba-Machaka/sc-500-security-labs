import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Get the Key Vault URL from environment variable
key_vault_url = "https://kv-sc500-secure-mtcm.vault.azure.net/"

print("[*] Authenticating...")

credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_url, credential=credential)

try:
    secret = client.get_secret("dbpassword")
    print(f"[+] Success! Secret value is: {secret.value}")
except Exception as e:
    print(f"[-] Access Blocked: {e}")
