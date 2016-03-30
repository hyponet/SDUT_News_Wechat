#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient

from app import HOST, PORT, DATABASE, USERNAME, PASSWORD

def update_user(user):
    client = MongoClient(host=HOST, port=int(PORT))
    db = client[DATABASE]
    if USERNAME is not None:
        db.authenticate(USERNAME, PASSWORD, DATABASE, mechanism='MONGODB-CR')

    try:
        db['account'].update(
        {
            'id': user['id']
        },
        user,
        upsert=True    
        )
        return True
    except:
        pass
    return False


def get_user(id):
    client = MongoClient(host=HOST, port=int(PORT))
    db = client[DATABASE]
    if USERNAME is not None:
        db.authenticate(USERNAME, PASSWORD, DATABASE, mechanism='MONGODB-CR')

    try:
        userinfo = db['account'].find_one({'id': id})
    except:
        userinfo = None

    return dict(userinfo)
