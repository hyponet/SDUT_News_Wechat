#!/usr/bin/env python
# coding=utf-8

import json
import request

def get_point(user):
    no = user['no']
    URL = "http://gpa.updev.cn/api"

    req = request.post(URL, data={'no': no})
    userinfo = json.loads(req.text)

    return userinfo
