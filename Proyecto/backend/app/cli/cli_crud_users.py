'''CRUD operations for the CLI demo program of the ProjecTrack API.'''

import requests
import datetime
import json

## CRUD operations for users independent of roles
def add_user(API_URL, user):
    url = f"{API_URL}/users/add/"
    response = requests.post(url, json=user)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_user(API_URL, user_id):
    url = f"{API_URL}/users/get/{user_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()

def update_user(API_URL, user_id, updates):
    url = f"{API_URL}/users/update/{user_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_user(API_URL, user_id):
    url = f"{API_URL}/users/delete/{user_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_users(API_URL):
    url = f"{API_URL}/users/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()
