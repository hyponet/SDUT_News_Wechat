#!/usr/bin/env python
# coding=utf-8

import json
import requests

def get_point(user):
    no = user['no']
    URL = "http://gpa.updev.cn/api"

    req = requests.post(URL, data={'no': no})
    userinfo = json.loads(req.text)

    return userinfo
