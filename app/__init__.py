#!/usr/bin/env python
# coding=utf-8

from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'FUCKTHEGRADEPOINT'

APPID = os.getenv('APPID') or 'wx64a1e9e7a16828da'
APPSECRET = os.getenv('APPSECRET') or 'fd5712b4ca3ff65f6414f9953d370f15'

import index
