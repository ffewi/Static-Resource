<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
</style>
<!-- ## 解决运行jar包时 xxx.class.getResource获取对象为Null -->
> 执行命令：

__java -jar xxx.jar 或者 java -cp xxx.jar xxx.xxx.method__

> 源码：

``` java
public class GetResource {

    public static void main(String[] args) {
        // 获取相对路径，相对于当前类的路径--包
        URL relUrl = GetResource.class.getResource("");
        if (relUrl == null) {
            System.out.println("当前获取路径对象  relUrl 为NULL!!!");
        } else {
            System.out.println("PATH:" + relUrl.getPath());
        }

        // 获取绝对路径，相对于当前项目的路径
        URL absUrl = GetResource.class.getResource("/");
        if (absUrl == null) {
            System.out.println("当前获取路径对象 absUrl 为NULL!!!");
        } else {
            System.out.println("PATH:" + absUrl.getPath());
        }

        // 获取相对子路径，相对于当前类的包的子路径
        URL subUrl = GetResource.class.getResource("sub/sub1");
        if (subUrl == null) {
            System.out.println("当前获取路径对象 subUrl 为NULL!!!");
        } else {
            System.out.println("PATH:" + subUrl.getPath());
        }

    }

}

```

> 还发工具Eclipse执行结果：

    PATH:/G:/yitongeclipse/MyDemo/bin/test/
    PATH:/G:/yitongeclipse/MyDemo/bin/
    PATH:/G:/yitongeclipse/MyDemo/bin/test/sub/sub1

> 打包成jar包执行结果：

```G:\jar>java -cp MyDemo.jar test.GetResource```

    当前获取路径对象 relUrl 为NULL!!!
    当前获取路径对象 absUrl 为NULL!!!
    当前获取路径对象 subUrl 为NULL!!!

> 打包成jar[勾选Add directory entries]包执行结果：

```G:\jar>java -cp MyDemo.jar test.GetResource```

    PATH:file:/G:/jar/MyDemo.jar!/test/
    当前获取路径对象 absUrl 为NULL!!!
    当前获取路径对象 subUrl 为NULL!!!


看到后面两个输出还是为NULL,解决方法：
右键项目->`properties`->`Project Facets`->勾选 `Utility Module`;
随后可在项目中看到自动生成 `META-INF` 文件夹并且包含 `MANIFEST.MF` 文件

编辑文件 `MANIFEST.MF`:

    Manifest-Version: 1.0
    Class-Path: .

> 执行结果：

```G:\jar>java -cp MyDemo.jar test.GetResource```

    PATH:file:/G:/jar/MyDemo.jar!/test/
    PATH:/G:/jar/
    当前获取路径对象 subUrl 为NULL!!!

可以看到，最后一个获取相对路径下的地址返回也是NULL；造成此结果原因为程序被打成jar后，已经不能看成目录来访问了。

<!-- md文档区域 END -->

<!-- 代码高亮 -->
<link href="../../css/md_code.min.css" rel="stylesheet">
<script src="../../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->