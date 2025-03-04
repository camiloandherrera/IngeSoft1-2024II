'''CRUD operations for the CLI demo program of the ProjecTrack API.'''

import requests
import datetime
import json


## CRUD operations for assignments
# Assignments
def add_assignment(API_URL, assignment):
    url = f"{API_URL}/assignments/add/"
    response = requests.post(url, json=assignment)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_assignment(API_URL, assignment_id):
    url = f"{API_URL}/assignments/get/{assignment_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()

def update_assignment(API_URL, assignment_id, updates):
    url = f"{API_URL}/assignments/update/{assignment_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_assignment(API_URL, assignment_id):
    url = f"{API_URL}/assignments/delete/{assignment_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_assignments(API_URL):
    url = f"{API_URL}/assignments/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()

# Student Assignments
def add_student_assignment(API_URL, student_assignment):
    url = f"{API_URL}/student_assignments/add/"
    response = requests.post(url, json=student_assignment)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_student_assignment(API_URL, assignment_id):
    url = f"{API_URL}/student_assignments/get/{assignment_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()

def update_student_assignment(API_URL, assignment_id, updates):
    url = f"{API_URL}/student_assignments/update/{assignment_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_student_assignment(API_URL, assignment_id):
    url = f"{API_URL}/student_assignments/delete/{assignment_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

## CRUD operations for submissions
# Submissions
def add_submission(API_URL, submission):
    url = f"{API_URL}/submissions/add/"
    response = requests.post(url, json=submission)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def get_submission(API_URL, submission_id):
    url = f"{API_URL}/submissions/get/{submission_id}"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()

def update_submission(API_URL, submission_id, updates):
    url = f"{API_URL}/submissions/update/{submission_id}"
    response = requests.put(url, json=updates)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

def delete_submission(API_URL, submission_id):
    url = f"{API_URL}/submissions/delete/{submission_id}"
    response = requests.delete(url)

    print("\nStatus Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))


def get_submissions(API_URL):
    url = f"{API_URL}/submissions/get/"
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    #print(json.dumps(response.json(), indent=4))

    return response.json()
