#!/usr/bin/env python
# coding=utf-8

from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'FUCKTHEGRADEPOINT'

import index
