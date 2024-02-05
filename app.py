import requests
import time

API_KEY = ‘insert api key’
ORG_ID = ‘insert ‘org id here
HEADERS = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

def get_networks():
    url = f'https://api.meraki.com/api/v1/organizations/{ORG_ID}/networks'
    response = requests.get(url, headers=HEADERS)
    print(f"Fetched {len(response.json())} networks")
    return response.json()

def get_users(network_id):
    url = f'https://api.meraki.com/api/v1/networks/{network_id}/merakiAuthUsers'
    response = requests.get(url, headers=HEADERS)
    print(f"Fetched {len(response.json())} users for network {network_id}")
    return response.json()

def get_emails_from_file():
    with open('name.txt', 'r') as file:
        return [line.strip() for line in file]

def main():
    networks = get_networks()
    emails = get_emails_from_file()
    results = []

    for network in networks:
        users = get_users(network['id'])
        time.sleep(0.2)  # to respect the rate limit
        for user in users:
            print(f"User email: {user['email']}")  # new line for debugging
            if user['email'] in emails:
                results.append({
                    'email': user['email'],
                    'network_id': network['id'],
                    'network_name': network['name']
                })

    for result in results:
        print(f"Email: {result['email']}, Network ID: {result['network_id']}, Network Name: {result['network_name']}")

if __name__ == "__main__":
    main()
