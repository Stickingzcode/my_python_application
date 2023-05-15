name = input('Enter your username: ')
print(name)
def email(name):
    new_name = name[:-10]
    return new_name
print(f'Your name is: {email(name)}')

# another way to go about it

def username_generator(email:str):
    username = email.split('@')[0]
    return f'your username is {username}'