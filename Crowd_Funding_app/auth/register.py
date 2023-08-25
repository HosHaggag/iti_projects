

import json
import re
import auth.activate as activate



def sign_up():
    try:
        first_name = "Hossam" # input('Enter your first name: ')
        last_name = "Haggag" # input('Enter your last name: ')
        email = "haggagdev@gmail.com"  #input('Enter your email: ')
        password = "aa123245" # input('Enter your password: ')
        mobile_number = "01010612562" # input('Enter your mobile number: ')
        error = validate_user_data(first_name, last_name, email, password ,mobile_number)
        if error:
            raise Exception(error)
        if check_email(email):
            raise Exception('Email is already in use.')
        if check_mobile_number(mobile_number):
            raise Exception('Mobile number is already in use.')
        user = save_user_data(first_name, last_name, email, password, mobile_number)
        password = activate.generate_random_pass_code()
        activate.send_verify_email(email, password)
        if not activate.check_pass_code(password):
            raise Exception('wrong code')
        activate.activate_account(email)
        return user
    except Exception as error:
        raise Exception(error)


######  1  ######

def validate_user_data(first_name, last_name, email, password ,mobile_number):
    if not first_name:
        return 'First name is required.'
    if not last_name:
        return 'Last name is required.'
    if not email:
        return 'Email is required.'
    if not password:
        return 'Password is required.'
    if not mobile_number:
        return 'Mobile number is required.'
    if len(first_name) < 2:
        return 'First name must be at least 2 characters.'
    if len(last_name) < 2:
        return 'Last name must be at least 2 characters.'
    if len(password) < 5:
        return 'Password must be at least 5 characters.'
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return 'Email is invalid.'
    if not re.match(r'^[0-9]{11}$', mobile_number):
        return 'Mobile number is invalid.'
    return None


######  2  ######

def check_email(email):
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user['email'] == email:
            return True
    return False

######  3  ######


def check_mobile_number(mobile_number):
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        
        users = []
    for user in users:
        if user['mobile_number'] == mobile_number:
            return True
    return False


######  4  ######


def save_user_data(first_name, last_name, email, password, mobile_number):
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'mobile_number': mobile_number,
        'is_active': False,
        'projects': [],
    }
    users.append(user)
    with open('users.json' , 'w') as file:
        json.dump(users, file, indent=4)
    return user




