
import base64
import json
import math
import random
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


## Activate User Account ##




def activate_account(email):
    if not is_account_active(email):
        password = generate_random_pass_code()
        send_verify_email(email, password)
        if not check_pass_code(password):
            return 'wrong code'
        return activate_account(email)







#####  1   ######



def is_account_active(email):
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user['email'] == email:
            return user['is_active']
    return False


#####   2    ######


def generate_random_pass_code():
    digits = "0123456789"
    OTP = ""
    for i in range (6):
        OTP += digits[math.floor(random.random()*10)]    
    return OTP


#####   3    ######


def send_verify_email(recipients, password):
    try:
        flow = InstalledAppFlow.from_client_secrets_file('client_creds.json', [
        "https://www.googleapis.com/auth/gmail.send"
        ])
        creds = flow.run_local_server(port=0)

        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText('verify code is : ', password  )
        message['to'] = recipients
        message['subject'] = 'verify code for your account'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        # message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
        return True
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None
        return False


#####   4    ######

def check_pass_code(passcode):
    while True:
        entered = input('Enter your code: ')
        if entered == '0':
            return False
        return True



#####   5    ######


def activate_account(email):
    try:
        with open('users.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user['email'] == email:
            user['is_active'] = True
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)
            return user
    return None

