#!/usr/bin/env python
# coding=utf-8

from flask import request, abort
import xml.etree.ElementTree as ET
import hashlib
import os

from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if request.args.get('timestamp') == None:
            return abort(403)
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = os.getenv("TOKEN") or 'weixin'
        li = [token, timestamp, nonce]
        li.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, li)
        hashcode = sha1.hexdigest()
        if hashcode == request.args.get('signature'):
            return echostr
        else:
            return abort(403)
    elif request.method == 'POST':
        message = request.data  # 接收用户消息
        root = ET.fromstring(message)  # 解析xml
        to_user_name = root.findall('ToUserName')[0].text  # 开发者账号
        from_user_name = root.findall('FromUserName')[0].text  # 用户微信id
        create_time = root.findall('CreateTime')[0].text  # 消息创建时间 （整型）
        message_type = root.findall('MsgType')[0].text  # 消息类型text
        content = root.findall('Content')[0].text  # 消息内容
        message_id = root.findall('MsgId')[0].text  # 消息的ID
        return """
        <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>1</ArticleCount>
        <Articles>
        <item>
        <Title><![CDATA[欢迎使用gotit]]></Title>
        <Description><![CDATA[系统检测到您并未绑定，点击此页面前去绑定。或者您并不想进行绑定，请点击菜单栏的‘无绑定查询’]]></Description>
        <Url><![CDATA[lvhuiyang.cn/wechat/building]]></Url>
        </item>
        </xml>""" % (from_user_name, to_user_name, create_time)
