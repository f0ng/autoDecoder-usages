---
created: 2023-07-02T18:51:27+08:00
updated: 2023-07-02T18:55:06+08:00
---
# 谷歌浏览器设置

调试模式启动chrome浏览器

windows

```powershell
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --remote-allow-origins=*
```

macos

```bash
sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --remote-allow-origins=*
```

# 第一步

python3 -m pip install -r req.txt

req.txt内容如下
```bash
Flask
pychrome
requests
```

安装需要的各种库

# 第二步

运行chrome_cdp.py并输入对应的参数
![](photo/Pasted%20image%2020230702185413.png)
解密和加密各可以为空，以满足一些站点请求是明文但响应不是明文

# 第三步

在插件中设置好各种值即可正常使用

# 注意事项

## title值要确保只能获取到一个

现有5个title

![](photo/Pasted%20image%2020230702185432.png)

![](photo/Pasted%20image%2020230702185426.png)

可以设置为666699、7777888、99999999999

不能设置为777、8888、999（因为这些在title中可以找到多个）

## 谷歌浏览器一定要是先以调试模式打开

先打开一个普通的谷歌浏览器在打开一个调试模式的谷歌浏览器不行，必须先以调试模式打开谷歌浏览器

### 参考链接
https://zhaomenghuan.js.org/blog/chrome-devtools.html#chrome-devtools-protocol

https://chromedevtools.github.io/devtools-protocol/tot/Debugger/
