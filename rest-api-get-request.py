import requests
import argparse

parser = argparse.ArgumentParser(description='Enter Token')
parser.add_argument("--token")
args = parser.parse_args()

url = "https://ramkannan.jfrog.io/artifactory/api/repositories"
token = args.token
print(token)

headers = {
    'user-agent': "vscode-restclient",
    'authorization': f"Bearer {token}"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)