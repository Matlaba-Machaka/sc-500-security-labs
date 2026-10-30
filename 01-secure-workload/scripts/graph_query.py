import requests
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Request an Entra ID token specifically scoped for Microsoft Graph
token_obj = credential.get_token("https://microsoft.com")

headers = {"Authorization": f"Bearer {token_obj.token}"}
# Call the Graph API to list tenant users
response = requests.get("https://microsoft.com", headers=headers)

print("[+] Microsoft Graph Data:")
print(response.json())
