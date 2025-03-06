'''Demo for the API endpoints using requests library in Python with CRUD
operations for users, roles and assignments. CLI demo for the early development
of the ProjecTrack API.'''

import cli_crud_users, cli_crud_roles, cli_crud_assignments
import cli_functions

import requests
import datetime

BASE_URL = "http://localhost:8000/"
TOKEN = None
CLASS_ID = 20 # Example class ID

def login():
    '''Login function for the user'''
    global TOKEN
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})

    if response.status_code != 200:
        TOKEN = response.json()["access_token"]
        print("🔓 Login successful!")
        return response.json()["token_type"], response.json()["access_token"], response.json()["role"]
        #response.json()["role"]
    else:
        print("🔒 Login failed. Please try again.")
        return None

def role_selection():
    '''Main menu: role selection for the user'''
    print("\nSelect a role:")
    print("1. 📖 Student")
    print("2. 🏫 Professor")
    print("3. 🪠 Admin")
    print("4. ❌ Exit")
    role = int(input("Enter the role number: "))
    return role

def user_selection(role):
    '''Secondary menu action: role menus'''
    if role == 1:
        student_menu()
    elif role == 2:
        professor_menu()
    elif role == 3:
        admin_menu()
    elif role == 4:
        print("👋 Goodbye!")
        exit()

def student_menu():
    '''Student menu demo'''
    submenu = True
    role = 1
    while submenu == True:
        print("\n📖 Student Menu")
        print("1. 📝 View Assignment List")
        print("2. 📋 Find an Assignment")
        print("3. ❌ Return to Main Menu")
        action = int(input("Enter the action number: "))

        while True:
            if action == 1:
                cli_functions.get_class_assignments(BASE_URL, CLASS_ID, role)
                break
            elif action == 2:
                cli_functions.get_one_assignment(BASE_URL, CLASS_ID, 1)
                break
            elif action == 3:
                submenu = False
                break

def professor_menu():
    '''Professor menu demo'''
    role = 2
    submenu = True
    while submenu == True:
        print("\n🏫 Professor Menu")
        print("1. 📝 Create Assignment")
        print("2. 👥 Assign Project/Assignment to specific Student(s)")
        print("3. 📋 Find an Assignment")
        print("4. ❌ Return to Main Menu")
        action = int(input("Enter the action number: "))
        while True:
            if action == 1:
                cli_functions.create_assignment(BASE_URL, CLASS_ID)
                break
            elif action == 2:
                cli_functions.assign_student_assignment(BASE_URL)
                break
            elif action == 3:
                cli_functions.get_one_assignment(BASE_URL, CLASS_ID, role)
                break
            elif action == 4:
                submenu = False
                break

def admin_menu():
    '''Admin menu demo'''
    role = 3
    submenu = True
    while submenu == True:
        print("\n🪠 Admin Menu")
        print("1. 🧍 Add User")
        print("2. 📋 View User List")
        print("3. 👥 Add Role")
        print("4. 📋 View Role List")
        print("5. ☠️ Remove User")
        print("6. 🌪️ Remove Role")
        print("7. 📋 View Assignment List")
        print("8. ❌ Return to Main Menu")

        action = int(input("Enter the action number: "))

        while True:
            if action == 1:
                cli_functions.add_user(BASE_URL)
                break
            elif action == 2:
                cli_functions.view_users(BASE_URL)
                break
            elif action == 3:
                cli_functions.add_role(BASE_URL)
                break
            elif action == 4:
                cli_functions.view_roles(BASE_URL)
                break
            elif action == 5:
                cli_functions.remove_user(BASE_URL)
                break
            elif action == 6:
                cli_functions.remove_role(BASE_URL)
                break
            elif action == 7:
                cli_functions.get_class_assignments(BASE_URL, CLASS_ID, role)
                break
            elif action == 8:
                submenu = False
                break

'''
if __name__ == "__main__":
    print("\n📓✍️ Welcome to ProjecTrack!(Early Demo)💻📊")

    login_result = login()

    if login_result:
        token_type, token, role = login_result
        TOKEN = token
    while True:
        # role = role_selection()
        if role == "student":
            role_number = 1
        elif role == "professor":
            role_number = 2
        elif role == "admin":
            role_number = 3

        user_selection(role)
'''


if __name__ == "__main__":
    print("\n📓✍️ Welcome to ProjecTrack!(Early Demo)💻📊")

    while True:
        role = role_selection()
        user_selection(role)
