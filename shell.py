import time
from filesystem import filesystem

'''----Startup----'''
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


account_created = False
user = ''
print(filesystem['/']['etc']['motd'][0].strip())
time.sleep(0.5)
account_creation()
time.sleep(0.5)




'''----Actual Shell lmao----'''

#----Cmd execution----
def xcute_cmd_cat(): # Also need to add functionality when no file is specified in prompt
    if len(cmd) == 2:
        if cmd[1] in current_directory:
            show = current_directory.get(cmd[1])
            # If the file is a string: print, else: fail.       Add support for other 'file' types
            #if isinstance(show, str):
                #print(''.join(show))
            print(''.join(show))
            #else:
                #print(f'cat: {cmd[1]}: No readable data')

        else:
            print(f'cat: {cmd[1]}: No such file or directory')
        
        
    else:
        print("Sorry, I haven't added full cat functionality yet :(")
        print('cat: usage: cat [FILE]')

def xcute_cmd_newcd():
    global current_directory, current_directory_display
    print('Waring! This command may result in an error. It is not done.')
    if len(cmd) < 2:
        current_directory = filesystem['/']
        current_directory_display = '/'

    elif len(cmd) == 2:
        path = cmd[1]
        parts = path.split('/')
        #for 
    #elif cmd[1] in filesystem:
        


def xcute_cmd_cd(): # Fix: cd /bin, INSTEAD OF cd bin | MAKE SIMILAR TO ACTUAL UNIX WHERE ITS NOT 1 AT A TIME: /etc -> /etc/motd, -**NOT etc -> motd**-
    global current_directory, current_directory_display

    if len(cmd) < 2:
        current_directory = filesystem['/']
        current_directory_display = '/'
    elif cmd[1] in current_directory:
        current_directory = current_directory[cmd[1]]
        current_directory_display = current_directory_display + cmd[1] + '/'
    
    else:  
        print(f'cd: {cmd[1]}: No such file or directory')

def xcute_cmd_ls():
    if len(cmd) < 2:
        items = list(current_directory.keys())
        print('  '.join(items))

def xcute_cmd_mkdir():                                                  #TODO
    global current_directory, current_directory_display, filesystem
    filesystem.update()
    


def xcute_cmd_pwd():
    if len(cmd) > 1:
        if cmd[1] == '--shell' or cmd[1] == '-s':
            print(current_directory)
        else:
            print(f'Invalid option: {cmd[1]}')
            print('pwd: usage: pwd [-s]')

    else:
        print(current_directory_display)

def xcute_cmd_whoami():
    print(user)


#------CMD Dictionary------------

cmd_list_dic = {
    'cat': xcute_cmd_cat,            
    'newcd': xcute_cmd_newcd,
    "cd": xcute_cmd_cd,
    "ls": xcute_cmd_ls,
    "pwd": xcute_cmd_pwd,
    'mkdir': xcute_cmd_mkdir,
    'whoami': xcute_cmd_whoami       
}

def cmd_list_func():
    #if cmd[0] in filesystem['/']['bin']:       #This is for bin implimentation (for Lilly: see notes.txt)
        #filesystem['/']['bin'][cmd[0]]()
    if cmd[0] in cmd_list_dic:
        cmd_list_dic[cmd[0]]()
    else:
        print(f'{cmd[0]}: Command not found')



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


while True:
    shell()
