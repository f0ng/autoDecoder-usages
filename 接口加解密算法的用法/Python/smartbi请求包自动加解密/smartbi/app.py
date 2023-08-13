# -*- coding:utf-8 -*-  
# author:NaTsUk0
# @Date: 2022/11/11 下午14:25


# smartbi加解密实现
# 明文为  
# {"encode":"sysConfService.renewalSession+%5B%22u_41707964b0664542b783eca32f319e5f-11%22%5D","r":0.7287782339312623}
# 密文为  
# {"encode":"D2Dtw6_Wp4gRipq4p6pb(SWpDDRw6+/JV/uuQyK1979mMK~7MMKJKu~9'Npi(Nu_N1mpJ_f11/uu/JT","r":0.7287782339312623}


from flask import Flask, Response, request
import re

app = Flask(__name__)


@app.route('/encode', methods=["POST"])
def encrypt():
    body = request.form.get('dataBody')  # 获取  post 参数 必需  
    # headers = request.form.get('dataHeaders')  # 获取  post 参数  可选

    enc = {
        "0": "7", "1": "1", "2": "u", "3": "N", "4": "K", "5": "J", "6": "M", "7": "9", "8": "'", "9": "m", "!": "P",
        "%": "/", "'": "n", "(": "A", ")": "E", "*": "s", "+": "+", "-": "f", ".": "q", "A": "O", "B": "V", "C": "t",
        "D": "T", "E": "a", "F": "x", "G": "H", "H": "r", "I": "c", "J": "v", "K": "l", "L": "8", "M": "F", "N": "3",
        "O": "o", "P": "L", "Q": "Y", "R": "j", "S": "W", "T": "*", "U": "z", "V": "Z", "W": "!", "X": "B", "Y": ")",
        "Z": "U", "a": "(", "b": "~", "c": "i", "d": "h", "e": "p", "f": "_", "g": "-", "h": "I", "i": "R", "j": ".",
        "k": "G", "l": "S", "m": "d", "n": "6", "o": "w", "p": "5", "q": "0", "r": "4", "s": "D", "t": "k", "u": "Q",
        "v": "g", "w": "b", "x": "C", "y": "2", "z": "X", "~": "e", "_": "y",
    }

    plain_text = re.compile(r'(?<="encode":")(.*?)(?=",")') if len(re.compile(r'(?<="encode":")(.*?)(?=",")').findall(body)) != 0 else re.compile(r'(?<="data":")(.*?)(?=",")')

    out = ''
    for item in plain_text.findall(body)[0]:
        out += enc.get(item, item)

    return plain_text.sub(out, body)


@app.route('/decode', methods=["POST"])
def decrypt():
    body = request.form.get('dataBody')  # 获取  post 参数 必需  
    # headers = request.form.get('dataHeaders')  # 获取  post 参数  可选
    print(body)

    dec = {
        "7": "0", "1": "1", "u": "2", "N": "3", "K": "4", "J": "5", "M": "6", "9": "7", "'": "8", "m": "9", "P": "!",
        "/": "%", "n": "'", "A": "(", "E": ")", "s": "*", "+": "+", "f": "-", "q": ".", "O": "A", "V": "B", "t": "C",
        "T": "D", "a": "E", "x": "F", "H": "G", "r": "H", "c": "I", "v": "J", "l": "K", "8": "L", "F": "M", "3": "N",
        "o": "O", "L": "P", "Y": "Q", "j": "R", "W": "S", "*": "T", "z": "U", "Z": "V", "!": "W", "B": "X", ")": "Y",
        "U": "Z", "(": "a", "~": "b", "i": "c", "h": "d", "p": "e", "_": "f", "-": "g", "I": "h", "R": "i", ".": "j",
        "G": "k", "S": "l", "d": "m", "6": "n", "w": "o", "5": "p", "0": "q", "4": "r", "D": "s", "k": "t", "Q": "u",
        "g": "v", "b": "w", "C": "x", "2": "y", "X": "z", "e": "~", "y": "_",
    }

    plain_text = re.compile(r'(?<="encode":")(.*?)(?=",")') if len(re.compile(r'(?<="encode":")(.*?)(?=",")').findall(body)) != 0 else re.compile(r'(?<="data":")(.*?)(?=",")')

    out = ''
    for item in plain_text.findall(body)[0]:
        out += dec.get(item, item)

    return plain_text.sub(out, body)


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(host="0.0.0.0", port=8888)
