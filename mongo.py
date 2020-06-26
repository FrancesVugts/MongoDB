import os
from os import path
if path.exists("env.py"):
    import env

MONGO_URI = os.environ.get('MONGO_URI')
