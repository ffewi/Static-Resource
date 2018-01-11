<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
</style>

## Connect to MySQL(MariaDB)
windows 使用Navicat for Mysql连接Linux环境下的Mysql(MariaDB)

+ 首先在linux环境下安装 MariaDB,步骤省略。
+ 安装[Navicat for Mysql](http://www.navicat.com.cn/products/navicat-for-mysql 'Navicat for Mysql')
<center>![Navicat for Mysql](../pic/navicat/Navicat_for_Mysql%E6%88%AA%E5%9B%BE.png 'Navicat for Mysql')</center>
+ 配置SSH    
    由于Linux服务不允许外部IP地址直接访问，需要用SSH通道连接转为本地连接。
<center>![配置SSH通道](../pic/navicat/SSH%E8%BF%9E%E6%8E%A5%E9%85%8D%E7%BD%AE.png '配置SSH通道')</center>

+ 配置常规配置
    就像本机配置连接Mysql一样
<center>![常规配置](../pic/navicat/Mysql%E5%B8%B8%E8%A7%84%E9%85%8D%E7%BD%AE.png '常规配置')</center>

+ 连接成功    
<center>![连接成功](../pic/navicat/%E8%BF%9E%E6%8E%A5mysql%E5%AE%8C%E6%88%90.png '连接成功')</center>


## 小Tips

如何查看mysql启用端口


1. 去找到解压Mysql的目录文件，找到my.ini文件，查看<code>port=??</code>配置

2. 执行sql命令获取port。例如：

        show variables like 'port';

| Variable_name | Value |
| ------------- | ----- |
| port          | 3306  |

<!-- 代码高亮 -->
<link href="../css/md_code.min.css" rel="stylesheet">
<script src="../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>
<!-- 代码高亮结束 -->
