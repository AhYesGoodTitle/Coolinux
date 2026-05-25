'''----Pre recs----'''
import time
from account_setup import account_creation, login, user, password
from filesystem import filesystem

'''----Startup----'''
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
