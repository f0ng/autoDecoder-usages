# -*- coding:utf-8 -*-  
# author:f0ngf0ng  
# @Date: 2022/5/15 下午10:25


# 3des加密实现
# 明文为  
# {'username':'admin'}  
#  
# 密文为  
# 5Pne6rhiOkxfngbJMpSc+aBCaNE/09HW  

import re


def encrypt(body):
    enc = {
        "0": "7", "1": "1", "2": "u", "3": "N", "4": "K", "5": "J", "6": "M", "7": "9", "8": "'", "9": "m", "!": "P",
        "%": "/", "'": "n", "(": "A", ")": "E", "*": "s", "+": "+", "-": "f", ".": "q", "A": "O", "B": "V", "C": "t",
        "D": "T", "E": "a", "F": "x", "G": "H", "H": "r", "I": "c", "J": "v", "K": "l", "L": "8", "M": "F", "N": "3",
        "O": "o", "P": "L", "Q": "Y", "R": "j", "S": "W", "T": "*", "U": "z", "V": "Z", "W": "!", "X": "B", "Y": ")",
        "Z": "U", "a": "(", "b": "~", "c": "i", "d": "h", "e": "p", "f": "_", "g": "-", "h": "I", "i": "R", "j": ".",
        "k": "G", "l": "S", "m": "d", "n": "6", "o": "w", "p": "5", "q": "0", "r": "4", "s": "D", "t": "k", "u": "Q",
        "v": "g", "w": "b", "x": "C", "y": "2", "z": "X", "~": "e", "_": "y",
    }

    plain_text = re.compile(r'(?<="encode":")(.*?)(?=",")') if re.compile(r'(?<="encode":")(.*?)(?=",")').findall(body) is False else re.compile(r'(?<="data":")(.*?)(?=",")')

    print(plain_text)

    out = ''
    for item in plain_text.findall(body):
        out += enc.get(item, item)

    return plain_text.sub(out, body)


def decrypt(body):
    dec = {
        "7": "0", "1": "1", "u": "2", "N": "3", "K": "4", "J": "5", "M": "6", "9": "7", "'": "8", "m": "9", "P": "!",
        "/": "%", "n": "'", "A": "(", "E": ")", "s": "*", "+": "+", "f": "-", "q": ".", "O": "A", "V": "B", "t": "C",
        "T": "D", "a": "E", "x": "F", "H": "G", "r": "H", "c": "I", "v": "J", "l": "K", "8": "L", "F": "M", "3": "N",
        "o": "O", "L": "P", "Y": "Q", "j": "R", "W": "S", "*": "T", "z": "U", "Z": "V", "!": "W", "B": "X", ")": "Y",
        "U": "Z", "(": "a", "~": "b", "i": "c", "h": "d", "p": "e", "_": "f", "-": "g", "I": "h", "R": "i", ".": "j",
        "G": "k", "S": "l", "d": "m", "6": "n", "w": "o", "5": "p", "0": "q", "4": "r", "D": "s", "k": "t", "Q": "u",
        "g": "v", "b": "w", "C": "x", "2": "y", "X": "z", "e": "~", "y": "_",
    }

    # plain_text = re.compile(r'(?<="encode":")(.*?)(?=",")') if len(re.compile(r'(?<="encode":")(.*?)(?=",")').findall(body)) != 0 else re.compile(r'(?<="data":")(.*?)(?=",")')
    #
    # print(plain_text)
    #
    # out = ''
    # for item in plain_text.findall(body)[0]:
    #     out += dec.get(item, item)
    #
    # print(out)
    #
    # return plain_text.sub(out, body)

    out = ''
    for item in body:
        out += dec.get(item, item)

    return out


if __name__ == '__main__':
    # body='{"encode":"D2Dtw6_Wp4gRipq4p6pb(SWpDDRw6+/JV/uuQyK1979mMK~7MMKJKu~9\'Npi(Nu_N1mpJ_f11/uu/JT","r":0.7287782339312623}'
    # body = '{\"code\":0,\"data\":\"{\"IOm~\":q,\"9*v\":\"\",\"~9*v\":\"\",\"mECE\":{\"eEv~lcU~\":1q,\"eEv~329w~H\":q,\"COCEK!Ev~*\":1,\"COCEK)K~9~\'C*\":q,\"*cU~\":1q,\"\'29w~H\":q,\"\'29w~HA-)K~9~\'C*\":q,\"KE*C\":CH2~,\"-cH*C\":CH2~,\"IO'C~'C\":[]},\"Cc9~\":np}\",\"time\":0}'
    body = input()
    print(decrypt(body))
