'''----Pre recs----'''
import time
from filesystem import filesystem

'''----Startup----'''
# Pre recs
account_created = False
user = ''

# Account functions
def account_creation():
    global user, account_created, password

    if account_created == False:
        while True:
            if user == '':
                user = input('Please enter a username: ')
                continue
            elif ' ' in user:
                print('Username cannot have a space')
                user = input('Please enter a username: ')
                continue
            else:
                break
        print('')
        password = input(f'Please enter a strong password for {user}: ')
        while True:
            if password == "":
                password = input(f'Please enter a strong password for {user}: ')
                continue
            else:
                account_created = True
                print('')
                print('Account created successfully. Now sign in...')
                print ('')
                break

def login():
    global logged_in
    if account_created == True:
        command = input('Enter username: ')
        while True:
            if command == user:
                command = input(f'Enter password for {user}: ')
                if command == password:
                    logged_in = True
                    break
                else:
                    print(f'Incorrect password for: "{user}"')
                    command = input(f'Enter password for {user}: ')
            else:
                print(f'Username: {command} not found')
                command = input('Enter username: ')


# Create account; *add login aswell*
print('''
Welcome to Coolinux :3
This is a unix inspired "VM" made in python!
Check the git page for more technical information, disclaimers, and source code.

You can edit the startup message in /etc/motd
''')
time.sleep(0.5)
account_creation()
time.sleep(0.5)
login()


