#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient
import json

# from app import HOST, PORT, DATABASE, USERNAME, PASSWORD
import os
HOST = os.getenv('MONGODB_PORT_27017_TCP_ADDR') or '127.0.0.1'
PORT = os.getenv('MONGODB_PORT_27017_TCP_PORT') or 27017
DATABASE = os.getenv('MONGODB_INSTANCE_NAME') or 'TEST'
USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = os.getenv('MONGODB_PASSWORD')

def update_user(user):
    client = MongoClient(host=HOST, port=int(PORT))
    if USERNAME is not None:
        db = client[DATABASE].authenticate(USERNAME, PASSWORD, DATABASE, mechanism='MONGODB-CR')
    else:
        db = client[DATABASE]

#    return db
    try:
        print db
    except:
        pass
    return json.dumps(user)


if __name__ == '__main__':
    print update_user([])

