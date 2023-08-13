---
created: 2023-08-13T14:53:51+08:00
updated: 2023-08-13T14:53:51+08:00
---
# 使用burp插件autoDecoder实现对smartbi请求包自动加解密

# 安装autoDecoder插件

github下载的在新版burp会有bug，请使用压缩包中的插件安装

# 编写针对smartbi的加解密脚本

因为它的加解密都是一对一替换，所以很简单，就实现加解密两个函数就行了，脚本也在压缩包里。

# 启动加解密脚本

插件里写的是8888端口，怎么改启动端口自己去百度。

# 选择使用接口进行加解密

如图
![1](photo/1.png)

# 设置监控域名及明密文关键词

smartbi特征比较明显
![image.png](photo/2.png)

# 然后就实现自动加解密了

脚本见[这里](https://github.com/f0ng/autoDecoder-usages/tree/main/%E6%8E%A5%E5%8F%A3%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84%E7%94%A8%E6%B3%95/Python/smartbi%E8%AF%B7%E6%B1%82%E5%8C%85%E8%87%AA%E5%8A%A8%E5%8A%A0%E8%A7%A3%E5%AF%86/smartbi)
