<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
    span.linkId{
        color: purple;
    }

    span.linkId:hover{
        color:orange;
        cursor: pointer;
    }

    span.pink-weak{
        color: hsl(300,55%,80%);
    }
</style>

<!-- 正文 -->
*  ## 第 1 章 编程基础和字符串
    - <span class="linkId" data-id='1-1'>1.1 编程与使用计算机的区别</span>
        + <span class="linkId pink-weak" data-id='1-1-1'>1.1.1 编程的一致性</span>
        + <span class="linkId pink-weak" data-id='1-1-2'>1.1.2 编程的可控性</span>
        + <span class="linkId pink-weak" data-id='1-1-3'>1.1.3 程序要对应变化</span>
        + <span class="linkId pink-weak" data-id='1-1-4'>1.1.4 小结</span>
    - <span class="linkId" data-id='1-2'>1.2 准备工作</span>
        + <span class="linkId pink-weak" data-id='1-2-1'>1.2.1 在非Windows系统上安装Python 3.*</span>
        + <span class="linkId pink-weak" data-id='1-2-2'>1.2.2 使用Python Shell</span>
    - <span class="linkId" data-id='1-3'>1.3 开始使用Python---字符串</span>
        + <span class="linkId pink-weak" data-id='1-3-1'>1.3.1 字符串的概述</span>
        + <span class="linkId pink-weak" data-id='1-3-2'>1.3.2 为什么要需要引号</span>
        + <span class="linkId pink-weak" data-id='1-3-3'>1.3.3 为什么有3种类型的引号</span>
        + <span class="linkId pink-weak" data-id='1-3-4'>1.3.4 使用print()函数</span>
        + <span class="linkId pink-weak" data-id='1-3-5'>1.3.5 理解不同的引号</span>
    - <span class="linkId" data-id='1-4'>1.4 串联两个字符串</span>
    - <span class="linkId" data-id='1-5'>1.5 用不同的方法串联字符串</span>
    - <span class="linkId" data-id='1-6'>1.6 本章小结</span>
    - <span class="linkId" data-id='1-7'>1.7 章节小练习</span>



<!-- 内容开始 -->
### <span id='1-1'>1.1 编程与使用计算机的区别</ span>
    啰嗦的介绍，此处省略500+字...
#### <span id='1-1-1'>1.1.1 编程的一致性</ span>
    繁琐的总结，干死省略300+字...
#### <span id='1-1-2'>1.1.2 编程的可控性</ span>
    Python 语言的一个目标就是实现模块化编程，后省略...200+
#### <span id='1-1-3'>1.1.3 程序要对应变化</ span>
    Python 提供了许多有用的特征，使得程序员可以描述出导致程序无法正常工作的原因。后省略...200+
#### <span id='1-1-4'>1.1.4 小结</ span>
    综上，一大堆文字语言。省略...100+
### <span id='1-2'>1.2 准备工作</ span>
    文字太多，直接给地址：www.python.org/download；自己选择一个合适的版本自己安装。开发学习工具：PyCharm(自己查)
#### <span id='1-2-1'>1.2.1 在非Windows系统上安装Python 3.*</ span>
    下载：www.python.org/download/mac；下好了自己安装。
#### <span id='1-2-2'>1.2.2 使用Python Shell</ span>
    又是一堆f话，后省略...300+
### <span id='1-3'>1.3 开始使用Python---字符串</ span>
    无关紧要的语言描述，后省略...200+
#### <span id='1-3-1'>1.3.1 字符串的概述</ span>
    字符串是 Python 语言的一种数据类型。后省略无关紧要描述...120+
    示例：
        "Hello ,2018 is a good year!"
        "1+1"
        "I'm handsome"
        "!@#$%^&*()"
#### <span id='1-3-2'>1.3.2 为什么要需要引号</ span>
    难以理解的描述，后省略...200+
#### <span id='1-3-3'>1.3.3 为什么有3种类型的引号</ span>
    一堆描述，省略...250+
    三种字符表示：
        1. ""
        2. ''
        3. """"""
        4. ''''''
#### <span id='1-3-4'>1.3.4 使用print()函数</ span>
    200+文字描述省略...
    API: print(value, ..., sep, end, file, flush)
    print('First to do it!')
#### <span id='1-3-5'>1.3.5 理解不同的引号</ span>
    300+文字描述省略...
    "" & '' :普通的引号，支持一行字符。
    """""" & '''''' :多好字符的引号，支持多行字符。
### <span id='1-4'>1.4 串联两个字符串</ span>
    描述太多，省略...260+
    总而言之，就是使用‘+’连接：'Hello' + ' boy' = 'Hello boy'
    或者，输出连接：print('Hello', 'boy')
### <span id='1-5'>1.5 用不同的方法串联字符串</ span>
| 占位符  |替换内容    |
|:-------:|------------|
| %d      |整数        |
| %f      |浮点数      |
| %s      |字符串      |
| %x      |十六进制整数|

    描述内容省略...400+
    比较特别的连接，像C、Java使用占位符一般：
    'Python is %s good language!' % 'a very' ==> 'Python is a very good language!'
    'Python is %s good %s!' % ('a very', 'language') ==> 'Python is a very good language!'
### <span id='1-6'>1.6 本章小结</ span>
    就是上面的标题所有介绍内容，省略...300+
### <span id='1-7'>1.7 章节小练习</ span>

1. 输入字符串：
    `'Hey Boss,\n\ton the office,\t\when the means is\n\t\t\t what'`
>   测试

        自己测试查看结果...

2. 使用print()函数 输出与上面一样的结果
>   测试

        自己测试查看结果...


<!-- 尾部引用 -->

<script src="./../../../../js/jquery.min.js"></script>
<script type="text/javascript">
// 友好的跳转链接 
    $('li>span.linkId').on('click', function(){
        var id = $(this).attr('data-id');
        $("html, body").animate({
            scrollTop: $("#"+id).offset().top }, 
            {duration: 500,easing: "swing"}
            );
    });
</script>
<!-- 代码高亮 -->
<link href="./../../../../css/md_code.min.css" rel="stylesheet">
<script src="./../../../../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->