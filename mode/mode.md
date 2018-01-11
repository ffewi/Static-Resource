<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
</style>

<!-- md文档区域 -->
#### 测试代码高亮显示
``` java
class Hello{
    private String name;

    public Hello(){
        this.name = "I'm good at you!";
    }

    public void say(){
        System.out.println("console.log：" + this.name);
    }
}
```

``` python
#e6601d
print('hello', 'man', seq='\n')
arr = [1, '2', {'name': 'test'}]
```
<!-- md文档区域 END -->

<!-- 代码高亮 -->
<link href="../css/md_code.min.css" rel="stylesheet">
<script src="../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->