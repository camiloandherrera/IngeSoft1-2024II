'''CRUD operations for the CLI demo program of the ProjecTrack API.'''

import requests
import datetime
import json

## CRUD operations for roles

def add_role(API_URL, role):
    url = f"{API_URL}/roles/add/"
    response = requests.post(url, json=role)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_role(API_URL, role_id):
    url = f"{API_URL}/roles/get/{role_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

def update_role(API_URL, role_id, updates):
    url = f"{API_URL}/roles/update/{role_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_role(API_URL, role_id):
    url = f"{API_URL}/roles/delete/{role_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_roles(API_URL):
    url = f"{API_URL}/roles/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()



## CRUD operations for professors and students
# Professors

def add_professor(API_URL, professor):
    url = f"{API_URL}/professors/add/"
    response = requests.post(url, json=professor)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_professor(API_URL, professor_id):
    url = f"{API_URL}/professors/get/{professor_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

def update_professor(API_URL, professor_id, updates):
    url = f"{API_URL}/professors/update/{professor_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_professor(API_URL, professor_id):
    url = f"{API_URL}/professors/delete/{professor_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_professors(API_URL):
    url = f"{API_URL}/professors/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

# Students

def add_student(API_URL, student):
    url = f"{API_URL}/students/add/"
    response = requests.post(url, json=student)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_student(API_URL, student_id):
    url = f"{API_URL}/students/get/{student_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

def update_student(API_URL, student_id, updates):
    url = f"{API_URL}/students/update/{student_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_student(API_URL, student_id):
    url = f"{API_URL}/students/delete/{student_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_students(API_URL):
    url = f"{API_URL}/students/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))
