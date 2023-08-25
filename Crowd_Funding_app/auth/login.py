import json
import re
import auth.register as register
import auth.activate as activate
from model.user import User
import setting



def login():
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    if not validate_email(email):
        return 'Email is invalid.'
    if not check_user_data(email,password):
        return 'Email or password is incorrect.'
    if not activate.is_account_active(email):    
        return 'Account is not active.'
    print('Welcome mr/miss ' + setting.user_data['first_name'] + ' ' + setting.user_data['last_name'] + ' you are logged in.')
    return None


def check_user_data(email,password):
    global user_data
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user['email'] == email and user['password'] == password  and user['is_active'] == True:
            setting.user_data = User(user)
            return True
    return False


def validate_email(email):
    if email == '':
        return False
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return False
    return True




