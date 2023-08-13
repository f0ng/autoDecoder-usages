# 0x01 使用

首先需要开启 Chrome 浏览器的远程调试功能，先退出现有的 Chrome 程序再执行以下命令

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

![1](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/1.png)

运行 node 服务器

![img](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/2.png)

访问 http://127.0.0.1:8888/debug 接口，测试当前 Hook 的调试页面

![3](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/3.png)

![image-20230813151751430](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/image-20230813151751430.png)

默认设置为 Hook 最新打开的标签页，如果需要 Hook 之前的页面可以修改脚本中默认的 pages 索引

![image-20230813150454109](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/image-20230813150454109.png)

# 0x02 参考

在浏览器中下断点，运行到指定函数位置时在 Console 中运行指令将函数提升为全局函数

![image-20230813150912861](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/image-20230813150912861.png)



![image-20230813150952394](chrome%20cdp%20%E5%8A%A0%E8%A7%A3%E5%AF%86.assets/image-20230813150952394.png)

PS: 全部函数设置完毕后==将浏览器调试断点放开，开启断点时会将脚本进程阻塞。使用过程中勿刷新页面，刷新页面后需重新提升函数==

然后就可以在 node 脚本里调用浏览器中的全局函数进行加解密操作了

# 0xFF Refer

https://pptr.dev/