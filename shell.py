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
                break


# Create account; *add login aswell*
print(filesystem['/']['etc']['motd'][0].strip())
time.sleep(0.5)
account_creation()
time.sleep(0.5)


'''----Actual Shell lmao----'''
#Pre recs
current_directory_display = '/'
current_directory = filesystem['/']

# Command split, and print current directory function
def shell():
    global cmd
    # print(" ".join(my_list))
    command = input(f'{user}@Coolinux:{current_directory_display} $ ')
    if command == '':
        shell()
    else:
        cmd = command.split()
        cmd_list_func()


#----Cmd execution after finding in dictionary (below)----

def xcute_cmd_cd():
    global current_directory, current_directory_display
    if len(cmd) < 2:
        current_directory = filesystem['/']
        current_directory_display = '/'
    elif cmd[1] in current_directory:  #impliment the current directory display, and make better logic ;-;
        current_directory = filesystem['/'][cmd[1]]
        print(current_directory)
    else:
        print(f'cd: {cmd[1]}: No such file or directory')
        print(f"current_directory: {current_directory}")
        print(f"cmd[1]: {cmd[1]}")
        print(list(current_directory.keys()))


#------------------

cmd_list_dic = {
    "cd": xcute_cmd_cd
}

def cmd_list_func():
    if cmd[0] in cmd_list_dic:
        cmd_list_dic[cmd[0]]()
    else:
        print(f'{cmd[0]}: Command not found')




while True:
    shell()
