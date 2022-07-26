import json
from os.path import exists

def get_credentials(credentials_directory, botname):
    if exists(credentials_directory):
        f = open(credentials_directory + '/' + botname + '.json', 'r')
        credentials = json.load(f)
        f.close()

        return credentials['token']
    else:
        return False


