## autodecoder用法及案例

	想维护成一个有很多用例、接口的项目，希望各位师傅有加解密之类的需求可以一起沟通，完善本项目。

	有些案例可能是旧版本下的autoDecoder举例，但是原理都是一样的，可以通过调试来判断是否达到了满意的效果

交流群

<img width="183" alt="image" src="https://user-images.githubusercontent.com/48286013/220634169-ddefd4b2-d967-4a85-8b28-b626ba366742.png">

链接失效可以添加微信`f-f0ng`，备注autoDecoder交流群

- ## autoDecoder的调试办法
  - #### [接口加解密调试](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E8%B0%83%E8%AF%95%E5%8A%9E%E6%B3%95/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E8%B0%83%E8%AF%95/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E8%B0%83%E8%AF%95.md)——举例说明
- ## 自带加解密算法的用法
	- #### [使响应包不解密1](https://github.com/f0ng/autoDecoder-usages/blob/main/%E8%87%AA%E5%B8%A6%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/%E4%BD%BF%E5%93%8D%E5%BA%94%E5%8C%85%E4%B8%8D%E8%A7%A3%E5%AF%861/%E4%BD%BF%E5%93%8D%E5%BA%94%E5%8C%85%E4%B8%8D%E8%A7%A3%E5%AF%861.md)——针对请求包有密文，响应包是明文的情况
	- #### [文本全加密(DES举例)](https://github.com/f0ng/autoDecoder-usages/blob/main/%E8%87%AA%E5%B8%A6%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/%E6%96%87%E6%9C%AC%E5%85%A8%E5%8A%A0%E5%AF%86/%E6%96%87%E6%9C%AC%E5%85%A8%E5%8A%A0%E5%AF%86.md)——针对请求包、响应包都为同一种加密方式
	- #### [指定文本加密(AES举例)](https://github.com/f0ng/autoDecoder-usages/blob/main/%E8%87%AA%E5%B8%A6%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/%E6%8C%87%E5%AE%9A%E6%96%87%E6%9C%AC%E5%8A%A0%E5%AF%86/%E6%8C%87%E5%AE%9A%E6%96%87%E6%9C%AC%E5%8A%A0%E5%AF%86.md)——使用正则匹配请求密文，响应包是明文的情况
- ## 接口加解密算法的用法
	- Python
		- #### [使响应包不解密2](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/%E4%BD%BF%E5%93%8D%E5%BA%94%E5%8C%85%E4%B8%8D%E8%A7%A3%E5%AF%862/%E4%BD%BF%E5%93%8D%E5%BA%94%E5%8C%85%E4%B8%8D%E8%A7%A3%E5%AF%862.md)——使用python的flask框架，针对请求包有密文，响应包是明文的情况
		- #### [登录数据包中LDAP加密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/%E7%99%BB%E5%BD%95%E5%8F%A3%E7%88%86%E7%A0%B4%E4%B9%8Bldap%E7%9A%84md5%E5%8A%A0%E5%AF%86/%E7%99%BB%E5%BD%95%E5%8F%A3%E7%88%86%E7%A0%B4%E4%B9%8Bldap%E7%9A%84md5%E5%8A%A0%E5%AF%86.md)——使用python的flask框架，配合`autoDecoder`插件、`captcha-killer-modified`插件爆破
		- #### [RSA解密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/RSA%E8%A7%A3%E5%AF%86/RSA%E8%A7%A3%E5%AF%86.md)——使用python的flask框架，解决分段RSA加密
		- #### [JSON嵌套加密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/JSON%E5%B5%8C%E5%A5%97%E5%8A%A0%E5%AF%86/JSON%E5%B5%8C%E5%A5%97%E5%8A%A0%E5%AF%86.md)——使用python的flask框架，解决json数据中嵌套一层base64编码的json加密数据的AES/ECB加解密
		- #### [通过Python执行Javascript加密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/%E9%80%9A%E8%BF%87py%E6%89%A7%E8%A1%8Cjs%E5%8A%A0%E5%AF%86/%E9%80%9A%E8%BF%87py%E6%89%A7%E8%A1%8Cjs%E5%8A%A0%E5%AF%86.md)——使用python的flask框架，解决一些Javascript的加密问题
		- #### [3DES加解密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/3DES%E5%8A%A0%E5%AF%86/3DES%E5%8A%A0%E5%AF%86.md)——使用python的flask框架，解决3DES/CBC加解密
	- Node
		- #### [SM4加解密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Node/sm4%E5%8A%A0%E5%AF%86/sm4%E5%8A%A0%E5%AF%86.md)——使用nodejs的http接口，解决SM4加解密
		- #### [AES加解密](https://github.com/f0ng/autoDecoder-usages/blob/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Node/AES%E5%8A%A0%E5%AF%86/AES%E5%8A%A0%E5%AF%86.md)——使用nodejs的http接口，解决AES/ECB加解密_另含有特殊关键字加解密处理方式
- ## autoDecoder的奇淫技巧
	- #### [绕过流量waf](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E5%A5%87%E6%B7%AB%E6%8A%80%E5%B7%A7/%E7%BB%95%E8%BF%87%E6%B5%81%E9%87%8Fwaf/%E7%BB%95%E8%BF%87%E6%B5%81%E9%87%8Fwaf.md)——使用python的flask框架，绕过waf对webshell的流量通信的阻断
	- #### [接口测试中替换参数](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E5%A5%87%E6%B7%AB%E6%8A%80%E5%B7%A7/%E6%9B%BF%E6%8D%A2%E5%8F%82%E6%95%B0/%E6%9B%BF%E6%8D%A2%E5%8F%82%E6%95%B0.md)——使用python的flask框架，解决自动测试接口中的批量参数替换问题
	- #### [sql注入绕过](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E5%A5%87%E6%B7%AB%E6%8A%80%E5%B7%A7/sql%E6%B3%A8%E5%85%A5%E7%BB%95%E8%BF%87%E4%B9%8Bsqlmap%E7%9A%84%E6%95%B0%E6%8D%AE%E5%8C%85%E6%8D%A2%E8%A1%8C%E9%97%AE%E9%A2%98/sql%E6%B3%A8%E5%85%A5%E7%BB%95%E8%BF%87%E4%B9%8Bsqlmap%E7%9A%84%E6%95%B0%E6%8D%AE%E5%8C%85%E6%8D%A2%E8%A1%8C%E9%97%AE%E9%A2%98.md)——使用python的flask框架，解决sqlmap的数据包换行问题
	- #### [POST自动转GET](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E5%A5%87%E6%B7%AB%E6%8A%80%E5%B7%A7/POST%E8%BD%ACGET/POST%E8%BD%ACGET.md)——使用python的flask框架，解决POST自动转GET问题 
	- #### [sqlmap的osshell遇到中文字符](https://github.com/f0ng/autoDecoder-usages/blob/main/autoDecoder%E7%9A%84%E5%A5%87%E6%B7%AB%E6%8A%80%E5%B7%A7/sqlmap%E7%9A%84osshell%E9%81%87%E5%88%B0%E4%B8%AD%E6%96%87%E5%AD%97%E7%AC%A6%E6%83%85%E5%86%B5/sqlmap%E7%9A%84osshell%E9%81%87%E5%88%B0%E4%B8%AD%E6%96%87%E5%AD%97%E7%AC%A6%E6%83%85%E5%86%B5.md)——使用python的flask框架，解决osshell中的出现中文目录无法正常执行命令的通病
- ## 脚本例子
  - #### [aes_cbc_zeropadding.py](https://github.com/f0ng/autoDecoder-usages/blob/main/%E5%8A%A0%E8%A7%A3%E5%AF%86%E4%BB%A3%E7%A0%81%E4%BE%8B%E5%AD%90/aes_cbc_zeropadding.py)——aes/cbc/零填充加密

## 写在最后
感谢xm17师傅提供脚本案例

