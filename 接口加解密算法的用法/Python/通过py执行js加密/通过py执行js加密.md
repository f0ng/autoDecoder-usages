---
created: 2023-02-03T14:58:51+08:00
updated: 2023-02-21T20:51:40+08:00
---
遇到一个js加密的登录框，js代码如下：
![](photo/Pasted%20image%2020230203145659.png)
遇到个密码加密，只有一个函数
```javascript
    function encode(_str) {
        var staticchars = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN";
        var encodechars = "";
        for (var i = 0; i < _str.length; i++) {
            var num0 = staticchars.indexOf(_str[i]);
            if (num0 == -1) {
                var code = _str[i];
            } else {
                var code = staticchars[(num0 + 3) % 62];
            }
            var num1 = parseInt(Math.random() * 62, 10);
            var num2 = parseInt(Math.random() * 62, 10);
            encodechars += staticchars[num1] + code + staticchars[num2];
        }
        return encodechars;
    }
```

直接利用python的execjs来执行，代码如下：
```python
# -*- coding: utf-8 -*-  
# @Time    : 2023/2/3 2:05 下午  
# @Software: f0ng  
  
  
from flask import Flask,request  
import execjs  
from urllib.parse import parse_qsl, parse_qs  
  
  
app = Flask(__name__)  
  
  
ctx = execjs.compile("""   
    function encode(_str) {        var staticchars = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN";        var encodechars = "";        for (var i = 0; i < _str.length; i++) {            var num0 = staticchars.indexOf(_str[i]);            if (num0 == -1) {                var code = _str[i];            } else {                var code = staticchars[(num0 + 3) % 62];            }            var num1 = parseInt(Math.random() * 62, 10);            var num2 = parseInt(Math.random() * 62, 10);            encodechars += staticchars[num1] + code + staticchars[num2];        }        return encodechars;    }  
""")  
  
@app.route('/encode',methods=["POST"])  
def encrypt():  
    total = ""  
    param = request.form.get('dataBody')  # 获取  post 参数  
    # print(param)
    dict = parse_qs(param)  
    en_pwd = ctx.call("encode", dict["password"][0])  
    # print(en_pwd)  
    dict["password"][0] = en_pwd  
    for key in dict.keys():  
        # print(key)  
        total = total + key + "=" + dict[key][0] + "&"  
  
    print(total[:-1])  
    return total[:-1]  
  
@app.route('/decode',methods=["POST"]) # 不解密  
def decrypt():  
    param = request.form.get('dataBody')  # 获取  post 参数  
    # print(param)    return param  
  
if __name__ == '__main__':  
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug  
    app.run(host="0.0.0.0",port="8888")
```
autodecoder配置如下：
![](photo/Pasted%20image%2020230203145800.png)

直接设置为明文密码就行了，intruder如下
![](photo/Pasted%20image%2020230203150042.png)

通过logger查看如下
![](photo/Pasted%20image%2020230203150117.png)
