### This script is not meant to be executed. It is merely a template that
### should be filled out and saved keys.py inside of a directory called secret.
### Be sure to include an empty __init__.py file in the secret directory so that
### the directory can be imported as a module.

## To create the Flask_Key, use os.urandom(45) from the os python standard
## library.
## To obtain Twitter credentials (consumer_secret, access_secret, access_token,
## consumer_key), go to https://dev.twitter.com/apps/new.

import os


def key():

    keys = {
        'Flask_Key': 'REPLACE WITH A KEY GENERATED BY OS',
        'consumer_secret': "REPLACE ME",
        'access_secret': "REPLACE ME",
        'access_token': "REPLACE ME",
        'consumer_key': "REPLACE ME"
    }

    return keys
