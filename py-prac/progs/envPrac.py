import os
from dotenv import load_dotenv

def env_load(file, pass2):
    file = input('Enter path to .env file: ');

    load_dotenv(file)
    pass2 = os.environ.get('PPASS')
    print(pass2)
