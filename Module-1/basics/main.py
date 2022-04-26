

users= []

def register():
    print('Please register a new user')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = {'username':username,'password':password}
    
    
    print(user)
    users.append(user)
    


def login():
    print('Please login using your username and password')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = None
    for i in users:
        if i['username'] == username and i['password'] == password:
            user = i
            break
    
    if user is None:
        print("Invalid username or password")
    
    elif user is not None:
        print("Welcome back, {}".format(user['username']))
    

register()

login()