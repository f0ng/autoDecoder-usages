# -*- coding:utf-8 -*-
# author:f0ngf0ng
import pychrome,time,re,os
import requests
from flask import Flask,Response,request
import base64,hashlib,json
#进行第二步延迟时间
times = 10

#远程cdp地址以下不需要变动
urls="http://127.0.0.1:9222"
callFrameId_str = ''
tab = None
title_str = ''
decrypt_str = ''
encrypt_str = ''
def cdp_encrypt(s):
    global title_str
    global decrypt_str
    global encrypt_str
    global tab
    encrypt_list = encrypt_str.split("%%%")
    print('当前加密函数：'+str(encrypt_list))
    print('当前加密写法：'+encrypt_list[0].replace(" ","")+"'"+s+"'"+encrypt_list[1])
    encrypt_string = tab.Debugger.evaluateOnCallFrame(callFrameId=callFrameId_str,expression=encrypt_list[0]+"'"+s+"'"+encrypt_list[1])['result']['value']
    return encrypt_string
        
def cdp_decrypt(s):
    global title_str
    global decrypt_str
    global encrypt_str
    global tab
    decrypt_list = decrypt_str.split("%%%")
    print('当前解密函数：'+str(decrypt_list))
    print('当前解密写法：'+decrypt_list[0]+"'"+s+"'"+decrypt_list[1])
    decrypt_string = tab.Debugger.evaluateOnCallFrame(callFrameId=callFrameId_str,expression=decrypt_list[0]+"'"+s+"'"+decrypt_list[1])['result']['value']
    return decrypt_string

app = Flask(__name__)

def setup():
    global title_str
    global decrypt_str
    global encrypt_str
    global tab
    title_str = input("请输入title（关键字即可）：")
    #title_str = '应用'
    decrypt_str = input('请输入解密代码(%%%为解密值)：')
    encrypt_str = input('请输入加密代码(%%%为加密值)：')

    def request_will_be_sent(**kwargs):
        global callFrameId_str
        return_kwargs = kwargs.get('callFrames')
        callFrameId_str_list = re.findall("'callFrameId': '(.*?)'",str(return_kwargs))
        callFrameId_str = callFrameId_str_list[0]
        print(f"callFrameId_str:{callFrameId_str_list[0]}")
    chrome = pychrome.Browser(url=urls)
    
    for _tab in chrome.list_tab():
        if title_str in _tab._kwargs['title']:
            tab = _tab
            url = urls+r'/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/'+str(tab).replace(r"<Tab [","").replace(r"]>","")
            print("调试地址：")
            print(url)
            tab.start()
            break
    if not tab:
        print('未发现可见TAB.')
     
    tab.Debugger.enable()
    print(f'进行第二步,当前延迟时间{str(times)}')
    tab.set_listener("Debugger.paused", request_will_be_sent)
    time.sleep(times)
with app.app_context():
    setup()
    
@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/encode',methods=["POST"])
def encrypt():
    global title_str
    global decrypt_str
    global encrypt_str
    if encrypt_str !="":
        param = request.form.get('dataBody')  # 获取  post 参数
        print('加密之前的值：'+str(param))
        encry_param = cdp_encrypt(param)
        print('加密之后的值：'+encry_param)
        return  encry_param
    else:
        param = request.form.get('dataBody')
        return param

@app.route('/decode',methods=["POST"]) # 不解密
def decrypt():
    global title_str
    global decrypt_str
    global encrypt_str
    if decrypt_str !="":
        param = request.form.get('dataBody')  # 获取  post 参数
        print('解密之前的值：'+str(param))
        decrypt_param = cdp_decrypt(param)
        print("解密之后的值："+decrypt_param)
        return decrypt_param
    else:
        param = request.form.get('dataBody')
        return param

if __name__ == '__main__':
    
    #app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host="0.0.0.0",port="8888")