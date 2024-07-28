

RC4流加密

登录前，请求头中的“Authorization”是加解密的密钥

![image-20240725003952423](./photo/image-20240725003952423.png)

登录后，用json格式，data存放加密数据，同时对数据包md5加密防篡改。请求头中的“Authorization: Bearer”是加密密钥，响应头中的“Current-Token”是解密密钥，一般情况下两个值是相等的。

![image-20240725004843898](./photo/image-20240725004843898.png)

当登录后，响应头中不存在“Current-Token：”，则使用固定的“zcareze”解密。出现这种情况请求包存在错误，服务器无法验证。

![image-20240725005410402](./photo/image-20240725005410402.png)

```
#js中的响应解密代码
if (200 === r.status) {
    let e = r.response;
    if (r.getResponseHeader("encryption") && e) {
        let t = r.getResponseHeader("current-token")
          , n = e;
        if ("string" == typeof e) {
            n = x(n, t || "zcareze");   #这里是响应头没有标志的密钥
            try {
                n = JSON.parse(n)
            } catch (e) {}
        }
        e = n
    }
    0,
    r.getResponseHeader("current-token") && C.update(r.getResponseHeader("current-token")),
    n(e)
```

**脚本存在缺陷，没有明确明文和密文，可能加密其他东西，需要等网站完全加载之后再开启接口**

![image-20240725005947376](./photo/image-20240725005947376.png)

python脚本如下：

```
# -*- coding:utf-8 -*-  
from flask import Flask,Response,request  
import re 
import json
import hashlib

def RC4(x, y):
    # 初始化状态数组 S 和索引 j
    z=[0] * 256
    A=len(y)
    B=len(x)
    for E in range(256):
        z[E] = E
    G = 0
    for E in range(256):
        G = (G + z[E] + ord(y[E % A])) % 256
        I = z[E]
        z[E], z[G] = z[G], I
    J = ''
    E = G = 0
    for K in range(B):
        E = (E + 1) & 255
        G = (G + z[E]) & 255
        L = ord(x[K])
        M = L ^ z[(z[E] + z[G]) % 256]
        J += chr(M)
        z[E], z[G] = z[G], z[E]
        G = (G + M + L) & 255
    return J
  
app = Flask(__name__)  
  
@app.route('/encode',methods=["POST"])  
def encrypt():  
    print('\n加密\n'+'-'*100)
    auth = request.form.get('dataHeaders')
    if 'Authorization: Bearer' in auth:  #判断密钥头是 Authorization: Bearer 或者 Authorization:
        pattern = r'Authorization: Bearer (\S+)'  #匹配Authorization: Bearer 4il9VEfg2JECgyhIYnh8gN8Q7iNvOiWFlQCFPTrSJD/GSef2k3SG56aTLQNh5rIuyFI/MisKk/JEKB1cMcsCldlrht94DejYvMFUxWciafPjPo+nxUsDPgyjMl33KE5taP5E/1X7v2FbfTzA4Xipq32hKtVBRnasobmtD3NbVts
    elif 'Authorization:' in auth:
        pattern = r'Authorization:\s+([a-fA-F0-9\-]+)'  #匹配2d59d42c-4790-4ee9-8877-2b597324efd3
    else:
        key = "8ac014c0-7f8e-424c-8402-11318d0cc0b6"   #这个不确定能不能用，用来占位的，如果请求包中没有密钥，根据实际情况修改
    key = re.findall(pattern,auth)[0]    #杜绝匹配不到key
    open('./tmp.txt', 'w').write(key)      #应对返回包请求头中没有加密密钥得情况，将密钥写入文件。特别不优雅，一点不优雅，有一定概率解决响应头中没有密钥的情况。

    body = request.form.get('dataBody')  # 获取  post 参数 必需
    body = eval("{}".format(body))       #直接转成字典，body = json.loads(body)  效果相同

    #sign 是否存在，sign是md5加密的
    if 'sign' not in body:    #简单的写前面，后面写否对参数进行md5加密
        body = RC4(str(body),key)
        return  auth + "\r\n\r\n\r\n" + body        #加密之后发包是三个"\r\n"
    else:
        #下面是对数据包的处理
        text = body['data']
        sign_text = "service={}&version=app&data={}&token={}".format(body['service'],text,key)
        md5_txt = hashlib.md5()
        md5_txt.update(sign_text.encode('utf-8'))
        print(md5_txt)
        body['data'] = RC4(text, key)
        body['sign'] = md5_txt.hexdigest()
        body = json.dumps(body)            #转回字符串
        return auth + "\r\n\r\n\r\n" + body

@app.route('/decode',methods=["POST"])  
def decrypt(): 
    print('\n解密\n'+'-'*100)
    iii = False   #用来判断需不需要保存密钥，可以改true，覆盖保存每次解密的密钥，只对响应头中没有密钥的情况有影响，
    auth = request.form.get('dataHeaders')
    if 'Authorization: Bearer' in auth:  #判断密钥头是 Authorization: Bearer 或者 Authorization:
        pattern = r'Authorization: Bearer (\S+)'  #匹配Authorization: Bearer 4il9VEfg2JECgyhIYnh8gN8Q7iNvOiWFlQCFPTrSJD/GSef2k3SG56aTLQNh5rIuyFI/MisKk/JEKB1cMcsCldlrht94DejYvMFUxWciafPjPo+nxUsDPgyjMl33KE5taP5E/1X7v2FbfTzA4Xipq32hKtVBRnasobmtD3NbVts
    elif 'Authorization:' in auth:
        pattern = r'Authorization:\s+([a-fA-F0-9\-]+)'  #匹配2d59d42c-4790-4ee9-8877-2b597324efd3
        iii = True
    elif 'Current-Token:' in auth:    #返回包中存放密钥的参数
        pattern = r'Current-Token:\s+(\S+)'
    elif 'Encryption:' in auth:
        key = 'zcareze'
        body = request.form.get('dataBody') # 为了逻辑简单清晰，继续不优雅，如果
        if '\\u' in body: body = eval("{}".format(body))   #消除加密中的"unicode"编码,body从获取到就是字符串，将"\u"转为"\\u"没办法正确解密。没有找到更好的办法
        body = RC4(body,key)    
        return auth + "\r\n\r\n\r\n\r\n" + body
    else:
        with open('./tmp.txt','r') as f:  #当响应头中没有参数的时候，尝试用tmp中保存的密钥解密
            key = f.read()
        body = request.form.get('dataBody') # 为了逻辑简单清晰，继续不优雅，如果
        if '\\u' in body: body = eval("{}".format(body))   #消除加密中的"unicode"编码,body从获取到就是字符串，将"\u"转为"\\u"没办法正确解密。没有找到更好的办法
        body = RC4(body,key)    
        return auth + "\r\n\r\n\r\n\r\n" + body
    key = re.findall(pattern,auth)[0]    #杜绝匹配不到key，提取json中内容,json中请求和响应都是带有密钥的，请求出错时没有密钥
    open('./tmp.txt', 'w').write(key) if iii else None      #应对返回包请求头中没有加密密钥得情况，将密钥写入文件。特别不优雅，一点不优雅。没有找到更好的办法

    #上面是获取key，下面是解密body

    body = request.form.get('dataBody') # 获取  post 参数 必需  
    # if '\\u' in body: body = eval("{}".format(body))   #和上面一样。
    if 'data":' in body: 
        body = eval("{}".format(body))
        text = body['data']   #提取body里面json加密的部分，根据实际情况修改”data“参数
        body['data'] = RC4(text,key)     #解密赋值
        return auth + "\r\n\r\n\r\n\r\n" + json.dumps(body)   #将body中的单引号转为双引号，看起来更好看
    elif '\\u' in body:
        body = eval("{}".format(body))
    body = RC4(body,key)    #解密赋值
    return auth + "\r\n\r\n\r\n\r\n" + body

# print(aes_encrypt('{"userName":"admin","userPwd":"123456"}'))  
if __name__ == '__main__':  
    app.run(host="0.0.0.0",port="8888")
```

原始响应包

![image-20240725011050364](./photo/image-20240725011050364.png)

解密如下：

![image-20240725010726297](./photo/image-20240725010726297.png)
