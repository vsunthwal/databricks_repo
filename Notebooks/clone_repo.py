import requests

# Read GitHub PAT securely from Databricks Secret Scope
token = dbutils.secrets.get(scope="my-github-scope", key="github-pat")

# Repo configuration
repo_url = "https://github.com/Lahari2223/Databricks.git"
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
repo_path = f"/Repos/{username}/Databricks_Repo"

# API endpoint
host = "https://adb-1231335714174499.19.azuredatabricks.net"  # Make sure this matches your workspace
api_url = f"{host}/api/2.0/repos"

# Request payload
headers = {"Authorization": f"Bearer {token}"}
payload = {
    "url": repo_url,
    "provider": "gitHub",
    "path": repo_path
}

# Clone repo
response = requests.post(api_url, headers=headers, json=payload)

# Handle response
if response.status_code == 200:
    print(f"✅ Repo cloned to: {repo_path}")
else:
    print(f"❌ Failed: {response.status_code} - {response.text}")
