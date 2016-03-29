#!/usr/bin/env python
# coding=utf-8

from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'FUCKTHEGRADEPOINT'

APPID = os.getenv('APPID') or 'wx64a1e9e7a16828da'
APPSECRET = os.getenv('APPSECRET') or 'fd5712b4ca3ff65f6414f9953d370f15'

# Mongo Config
HOST = os.getenv('MONGODB_PORT_27017_TCP_ADDR') or '127.0.0.1'
PORT = os.getenv('MONGODB_PORT_27017_TCP_PORT') or 27017
DATABASE = os.getenv('MONGODB_INSTANCE_NAME') or 'TEST'
USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = os.getenv('MONGODB_PASSWORD')

import index
