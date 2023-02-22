from flask import Flask
import base64
from Crypto.Cipher import AES
from flask import request

# 密钥（key）, 密斯偏移量（vi） CBC模式加密
app = Flask(__name__)
def AES_Encrypt(key, data):
    vi = '1234567890123456'
    pad = lambda s: s + (16 - len(s)%16) * chr(0)
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext

@app.route('/encrypt',methods=["POST"])
def encrypt():
    param = request.form.get('dataBody')  # 获取  post 参数

    print(param)
    encry_param = AES_Encrypt('1234567890123456',param)
    return encry_param

@app.route('/decode',methods=["POST"]) # 不解密
def decrypt():
    param = request.form.get('dataBody')  # 获取  post 参数
    return param


if __name__ == '__main__':
    app.run()
