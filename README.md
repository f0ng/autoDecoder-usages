## autodecoder用法及案例

有些案例可能是旧版本下的autoDecoder举例，但是原理都是一样的，可以通过调试来判断是否达到了满意的效果

- ## autoDecoder的调试办法
  - #### [接口加解密调试]——举例说明
- ## 自带加解密算法的用法
	- #### [使响应包不解密1]——针对请求包有密文，响应包是明文的情况
	- #### [文本全加密(DES举例)]——针对请求包、响应包都为同一种加密方式
	- #### [指定文本加密(AES举例)]——使用正则匹配请求密文，响应包是明文的情况
- ## 接口加解密算法的用法
	- Python
		- #### [使响应包不解密2]——使用python的flask框架，针对请求包有密文，响应包是明文的情况
		- #### [登录数据包中LDAP加密]——使用python的flask框架，配合`autoDecoder`插件、`captcha-killer-modified`插件爆破
		- #### [RSA解密]——使用python的flask框架，解决分段RSA加密
		- #### [JSON嵌套加密]——使用python的flask框架，解决json数据中嵌套一层base64编码的json加密数据的AES/ECB加解密
		- #### [通过Python执行Javascript加密]——使用python的flask框架，解决一些Javascript的加密问题
		- #### [3DES加解密]——使用python的flask框架，解决3DES/CBC加解密
	- Node
		- #### [SM4加解密]——使用nodejs的http接口，解决SM4加解密
		- #### [AES加解密]——使用nodejs的http接口，解决AES/ECB加解密_另含有特殊关键字加解密处理方式
- ## autoDecoder的奇淫技巧
	- #### [绕过流量waf]——使用python的flask框架，绕过waf对webshell的流量通信的阻断
	- #### [接口测试中替换参数]——使用python的flask框架，解决自动测试接口中的批量参数替换问题
	- #### [sql注入绕过]——使用python的flask框架，解决sqlmap的数据包换行问题
	- #### [POST自动转GET]——使用python的flask框架，解决POST自动转GET问题 
	- #### [sqlmap的osshell遇到中文字符]——使用python的flask框架，解决osshell中的出现中文目录无法正常执行命令的通病
- ## 脚本例子
  - #### aes_cbc_zeropadding.py



