import os
from dotenv import load_dotenv
# load_dotenv('./dev.env')

# env_file = input('Enter path to .env file: ')

# password = os.getenv('PPASS')
# password2 = os.environ.get('PUSER')

# print(password, password2)

def env_load(file, pass2):
    file = input('Enter path to .env file: ');

    load_dotenv(file)
    pass2 = os.environ.get('PPASS')
    print(pass2)
