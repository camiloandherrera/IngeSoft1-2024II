'''Role-specific menu functions, based on CRUD operations'''

import cli_crud_users, cli_crud_roles, cli_crud_assignments

import requests
import datetime

## Student functions
def get_class_assignments(API_URL, class_id, role):
    '''Get all assignments for a specific class'''
    request = cli_crud_assignments.get_assignments(API_URL)

    class_assignments = []
    for assignment in request:
        if assignment["class_id"] == class_id:
            class_assignments.append(assignment)

    print(f"\nClass {class_id} Assignments:\n")
    for assignment in class_assignments:
        print(f"Assignment ID: {assignment['_id']}")
        print(f"Title: {assignment['title']}")
        print(f"Description: {assignment['description']}")
        print(f"Assignment Date: {assignment['assignment_date']}")
        print(f"Deadline: {assignment['deadline']}")
        print("-" * 20)

        if role == 2 or role == 3:
            get_students_from_assignment(API_URL, assignment['_id'])



def get_students_from_assignment(API_URL, assignment_id):
    '''Get all students assigned to this assignment'''
    request = cli_crud_assignments.get_student_assignment(API_URL, assignment_id)

    try:
        student_ids = request['student_id']
    except:
        print(f"No specific students assigned to this assignment.\
            \nAll students in the class are assigned.")
        return

    students = []
    for student_id in student_ids:
        try:
            students.append(cli_crud_users.get_user(API_URL, student_id))
        except:
            print(f"Student ID {student_id} not found.")

    if students != []:
        print(f"\nAssignment {assignment_id} Students:\n")
        for student in students:
            print(f"Student ID: {student['_id']}")
            print(f"First Name: {student['first_name']}")
            print(f"Last Name: {student['last_name']}")
            print(f"Email: {student['email']}")
            print("-" * 20)


def get_one_assignment(API_URL, class_id, role):
    '''Get one assignment from the classby ID'''

    assignment_id = int(input("Enter the assignment ID: "))
    request = cli_crud_assignments.get_assignment(API_URL, assignment_id)

    if request["class_id"] != class_id:
        print(f"Assignment not found or not in your class.")
        return
    else:
        print(f"\nAssignment {assignment_id}:\n")
        print(f"Title: {request['title']}")
        print(f"Description: {request['description']}")
        print(f"Assignment Date: {request['assignment_date']}")
        print(f"Deadline: {request['deadline']}")

    if role == 2 or role == 3:
        get_students_from_assignment(API_URL, assignment_id)


## Professor functions
def create_assignment(API_URL, class_id):
    '''Create a new assignment'''
    print("\nCreating a new assignment:")

    assignment = {}

    assignment["assignment_id"] = int(input("Enter the assignment ID: "))
    assignment["title"] = input("Enter the assignment title: ")
    assignment["description"] = input("Enter the assignment description: ")
    assignment["assignment_date"] = str(datetime.date.today())
    assignment["deadline"] = input("Enter the assignment deadline (YYYY-MM-DD): ")
    if assignment["deadline"] == "":
        assignment["deadline"] = None
    assignment["class_id"] = class_id

    cli_crud_assignments.add_assignment(API_URL, assignment)

def assign_student_assignment(API_URL):
    '''Assign a student to an assignment'''
    print("\nAssigning a student to an assignment:")

    student_assignment = {}

    student_assignment["assignment_id"] = int(input("Enter the assignment ID: "))
    student_assignment["student_id"] = list(map(int, input("Enter the assignment IDs (comma-separated): ").split(',')))

    cli_crud_assignments.add_student_assignment(API_URL, student_assignment)


## Admin functions
def add_user(API_URL):
    '''Add a new user'''
    print("\nAdding a new user:")

    user = {}
    user["user_id"] = int(input("Enter the user ID: "))
    user["first_name"] = input("Enter the first name: ")
    user["middle_name"] = input("Enter the middle name: ")
    if user["middle_name"] == "":
        user["middle_name"] = None
    user["last_name"] = input("Enter the last name: ")
    user["second_last_name"] = input("Enter the second last name: ")
    if user["second_last_name"] == "":
        user["second_last_name"] = None
    user["email"] = input("Enter the email: ")
    user["password"] = input("Enter the password: ")
    user["role_id"] = int(input("Enter the role ID: "))
    user["sign_up_date"] = str(datetime.date.today())

    cli_crud_users.add_user(API_URL, user)


def view_users(API_URL):
    '''View all users'''
    request = cli_crud_users.get_users(API_URL)

    print("\nUsers:\n")
    for user in request:
        print(f"User ID: {user['_id']}")
        print(f"First Name: {user['first_name']}")
        print(f"Middle Name: {user['middle_name']}")
        print(f"Last Name: {user['last_name']}")
        print(f"Second Last Name: {user['second_last_name']}")
        print(f"Email: {user['email']}")
        print(f"Role ID: {user['role_id']}")
        print(f"Sign Up Date: {user['sign_up_date']}")
        print("-" * 20)

def add_role(API_URL):
    '''Add a new role'''
    print("\nAdding a new role:")

    role = {}
    role["role_id"] = int(input("Enter the role ID: "))
    role["role"] = input("Enter the role name: ")

    cli_crud_roles.add_role(API_URL, role)

def view_roles(API_URL):
    '''View all roles'''
    request = cli_crud_roles.get_roles(API_URL)

    print("\nRoles:\n")
    for role in request:
        print(f"Role ID: {role['_id']}")
        print(f"Role Name: {role['role']}")
        print("-" * 20)

def remove_user(API_URL):
    '''Remove a user'''
    user_id = int(input("Enter the user ID: "))
    cli_crud_users.delete_user(API_URL, user_id)

def remove_role(API_URL):
    '''Remove a role'''
    role_id = int(input("Enter the role ID: "))
    cli_crud_roles.delete_role(API_URL, role_id)
