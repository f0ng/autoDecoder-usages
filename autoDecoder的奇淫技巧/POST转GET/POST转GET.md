---
created: 2023-02-20T23:28:06+08:00
updated: 2023-02-20T23:49:28+08:00
---
## 背景
遇到一个shell，特点就是，post的shell传输会直接connection reset，而get就不会，这里传的是蚁剑的shell

post传payload无响应
![](photo/Pasted%20image%2020230220232937.png)


但是get传payload是有响应的
![](photo/Pasted%20image%2020230220233022.png)

但是蚁剑冰蝎没有将post转为get的按钮，burp也没有类似post自动转get的

写了一个Python的flask框架自动post转get请求，如下:
```Python
# -*- coding:utf-8 -*-  
# author:f0ngf0ng  
  
from flask import Flask,Response,request  
from pyDes import *  
import base64  
import hashlib  
import json  
import hmac  
import time  
  
  
  
app = Flask(__name__)  
  
@app.route('/encode',methods=["POST"])  
def encrypt():  
    param = request.form.get('dataBody')  # 获取  post 参数  
    param_headers = request.form.get('dataHeaders')  # 获取header参数  
    if param_headers != None:  
        headers0lists = param_headers.split("\n")[0].split(" ")[1]  
        headers0 = param_headers.split("\n")[0].split(" ")[0] + " " + param_headers.split("\n")[0].split(" ")[1] + "?" + param.strip() + " " + param_headers.split("\n")[0].split(" ")[2]  
  
        return param_headers.replace(param_headers.split("\n")[0],headers0) + "\r\n\r\n\r\n\r\n" + ""  
  
    return param  
  
@app.route('/decode',methods=["POST"])  
def decrypt():  
  
    param = request.form.get('dataBody')  # 获取  post 参数  
    param_headers = request.form.get('dataHeaders')  # 获取header参数  
    if param_headers != None:  
        return param_headers + "\r\n\r\n\r\n\r\n" + param  
  
    return param  
  
if __name__ == '__main__':  
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug  
    app.run(host="0.0.0.0",port="8888")
```
这里由于是只对请求包进行处理，所以只需要编写`encrypt()`函数即可
将以上文件保存为`app.py`文件，执行`python3 app.py`即可

配置页面如下:
![400](photo/Pasted%20image%2020230220233443.png)

调试页面如下：(这里使用加密调试，因为我们只需要加密模块)
![600](photo/Pasted%20image%2020230220233345.png)

原始请求:
![](photo/Pasted%20image%2020230220233520.png)

真实请求:(在logger模块可以看到)
![](photo/Pasted%20image%2020230220233546.png)

链接蚁剑代理也正常
![500](photo/Pasted%20image%2020230220234540.png)

