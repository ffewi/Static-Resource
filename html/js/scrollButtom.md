<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
</style>

# 鼠标滑动到底部事件

``` javascript
   window.onscroll = function () {    
            //监听事件内容
            var scrollTop = $(this).scrollTop();//滑动距离
            var scrollHeight = $(document).height();//当前网页对象的高度
            var windowHeight = $(this).height();//当前网页可视高度
            //滑动到底部判断
            if (scrollTop + windowHeight >= scrollHeight) {
                //处理的流程...
            }
        } 
```


<!-- md文档区域 END -->

<!-- 代码高亮 -->
<link href="../../css/md_code.min.css" rel="stylesheet">
<script src="../../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->