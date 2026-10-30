# Secure Azure Workload Lab (SC-500)

This project demonstrates how to run a Python application on an Azure Virtual Machine that securely retrieves secrets from an Azure Key Vault and queries Microsoft Graph **without storing any passwords, tokens, or credentials in the code**.

## 🏗️ What Was Built
*   **Azure Key Vault:** Stores our sensitive application database password.
*   **Managed Identity:** A passwordless identity assigned directly to our Azure VM.
*   **Network Firewall:** Key Vault access is locked down so only our specific VM can reach it.
*   **Azure Policy & Locks:** Guardrails that block public IP creation and prevent accidental deletion of our Key Vault.

---

## 🚀 How to Run the Scripts

Log into the Azure VM, open your terminal, install the required packages, and run the validation scripts:

```bash
pip install azure-identity azure-keyvault-secrets requests
```

### 1. Get Secret (`scripts/app.py`)
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your actual Key Vault URL
VAULT_URL = "https://azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

try:
    secret = client.get_secret("DatabasePassword")
    print(f"Success! Secret value is: {secret.value}")
except Exception as e:
    print(f"Access Denied: {e}")
```

### 2. Graph Query (`scripts/graph_query.py`)
```python
import requests
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://microsoft.com")
headers = {"Authorization": f"Bearer {token.token}"}

response = requests.get("https://microsoft.com", headers=headers)
print(response.json())
```

---

## 📸 Lab Proof & Screenshots

Here is the visual proof that the lab was successfully built and tested in Azure.

### 🔐 1. Key Vault & Identity Setup
*   **Secret Stored Successfully:** `![Secrets](./screenshots/01-keyvault-secrets.png)`
*   **Encryption Key Created:** `![Keys](./screenshots/02-keyvault-keys.png)`
*   **VM Managed Identity Turned On:** `![VM Identity](./screenshots/03-vm-managed-identity.png)`
*   **VM Granted Access to Key Vault:** `![Key Vault RBAC](./screenshots/04-keyvault-rbac.png)`

### 🛑 2. Network Hardening & Governance
*   **Key Vault Firewall Enabled:** `![Firewall](./screenshots/05-keyvault-firewall.png)`
*   **Delete Attempt Blocked by Lock:** `![Resource Lock](./screenshots/06-resource-lock-error.png)`
*   **Public IP Blocked by Azure Policy:** `![Azure Policy](./screenshots/07-azure-policy-denial.png)`

### 🧪 3. Successful Code Output
*   **Passwordless Script Execution Output:** `![Terminal Output](./screenshots/08-terminal-success.png)`