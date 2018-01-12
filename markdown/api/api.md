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

    thead tr th{
        font-family: '宋体';
        font-size: 12px;
        color:purple;
    }
    .markdown-body table tr:nth-child(2n){
        background-color: white;
    }
    .markdown-body table tr:hover{
        background-color: #f8f8f8;
    }

</style>
<!-- 导航 -->
## MarkDown 常用语法API
+ 转义
    - <span class="linkId" data-id='spacial_ch'>特殊字符</span>
+ 区块元素
    - <span class="linkId" data-id='dl_hh'>段落和换行</span>
    - <span class="linkId" data-id='title_ele'>标题</span>
    - <span class="linkId" data-id='bq_ele'>区块引用 Blockquotes</span>
    - <span class="linkId" data-id='list_ele'>列表</span>
    - <span class="linkId" data-id='code_ele'>代码区块</span>
    - <span class="linkId" data-id='cutLine_ele'>分隔线</span>
+ 区段元素
    - <span class="linkId" data-id='linkUrl_ele'>链接</span>
    - <span class="linkId" data-id='strong_ele'>强调</span>
    - <span class="linkId" data-id='codeSource_ele'>代码</span>
    - <span class="linkId" data-id='picture_ele'>图片</span>
+ 其它
    - <span class="linkId" data-id='autoLink_ele'>自动链接</span>
    - <span class="linkId" data-id='backslash_ele'>反斜杠</span>


<!-- 正文 -->
## 转义
#### <span id='spacial_ch'>特殊字符自动转换</span>

<center>常用字符转义对照表</center>
____
|字符|十进制|转义字符|
|:-----:|-----|-----|
|"|`&#34;`|`&quot;`|
|&|`&#38;`|`&amp;`|
|<|`&#60;`|`&lt;`|
|>|`&#62;`|`&gt;`|
|≤| |`&le;`|
|≥| |`&ge;`|
|不断开空格(non-breaking space)|`&#160;`|`&nbsp;`|
|☠|`&#9760;`||
|©| |`&copy;`|


<center>特殊转义字符对照表</center>
____

|字符|十进制|转义字符|字符|十进制|转义字符|字符|十进制|转义字符|
|:-----:|-----|-----|:-----:|-----|-----|:-----:|-----|-----|
|¡|`&#161;`|`&iexcl;`|Á|`&#193;`|`&Aacute;`|á|`&#225;`|`&aacute;`|
|￠|`&#162;`|`&cent;`|Â|`&#194;`|`&Acirc;`|â|`&#226;`|`&acirc;`|
|￡|`&#163;`|`&pound;`|Ã|`&#195;`|`&Atilde;`|ã|`&#227;`|`&atilde;`|
|¤|`&#164;`|`&curren;`|Ä|`&#196;`|`&Auml;`|ä|`&#228;`|`&auml;`|
|￥|`&#165;`|`&yen;`|Å|`&#197;`|`&Aring;`|å|`&#229;`|`&aring;`|
|¦|`&#166;`|`&brvbar;`|Æ|`&#198;`|`&AElig;`|æ|`&#230;`|`&aelig;`|
|§|`&#167;`|`&sect;`|Ç|`&#199;`|`&Ccedil;`|ç|`&#231;`|`&ccedil;`|
|¨|`&#168;`|`&uml;`|È|`&#200;`|`&Egrave;`|è|`&#232;`|`&egrave;`|
|©|`&#169;`|`&copy;`|É|`&#201;`|`&Eacute;`|é|`&#233;`|`&eacute;`|
|ª|`&#170;`|`&ordf;`|Ê|`&#202;`|`&Ecirc;`|ê|`&#234;`|`&ecirc;`|
|«|`&#171;`|`&laquo;`|Ë|`&#203;`|`&Euml;`|ë|`&#235;`|`&euml;`|
|¬|`&#172;`|`&not;`|Ì|`&#204;`|`&Igrave;`|ì|`&#236;`|`&igrave;`|
| |`&#173;`|`&shy;`|Í|`&#205;`|`&Iacute;`|í|`&#237;`|`&iacute;`|
|®|`&#174;`|`&reg;`|Î|`&#206;`|`&Icirc;`|î|`&#238;`|`&icirc;`|
|ˉ|`&#175;`|`&macr;`|Ï|`&#207;`|`&Iuml;`|ï|`&#239;`|`&iuml;`|
|°|`&#176;`|`&deg;`|Ð|`&#208;`|`&ETH;`|ð|`&#240;`|`&ieth;`|
|±|`&#177;`|`&plusmn;`|Ñ|`&#209;`|`&Ntilde;`|ñ|`&#241;`|`&ntilde;`|
|²|`&#178;`|`&sup2;`|Ò|`&#210;`|`&Ograve;`|ò|`&#242;`|`&ograve;`|
|³|`&#179;`|`&sup3;`|Ó|`&#211;`|`&Oacute;`|ó|`&#243;`|`&oacute;`|
|′|`&#180;`|`&acute;`|Ô|`&#212;`|`&Ocirc;`|ô|`&#244;`|`&ocirc;`|
|μ|`&#181;`|`&micro;`|Õ|`&#213;`|`&Otilde;`|õ|`&#245;`|`&otilde;`|
|¶|`&#182;`|`&para;`|Ö|`&#214;`|`&Ouml;`|ö|`&#246;`|`&ouml;`|
|·|`&#183;`|`&middot;`|×|`&#215;`|`&times;`|÷|`&#247;`|`&divide;`|
|¸|`&#184;`|`&cedil;`|Ø|`&#216;`|`&Oslash;`|ø|`&#248;`|`&oslash;`|
|¹|`&#185;`|`&sup1;`|Ù|`&#217;`|`&Ugrave;`|ù|`&#249;`|`&ugrave;`|
|º|`&#186;`|`&ordm;`|Ú|`&#218;`|`&Uacute;`|ú|`&#250;`|`&uacute;`|
|»|`&#187;`|`&raquo;`|Û|`&#219;`|`&Ucirc;`|û|`&#251;`|`&ucirc;`|
|¼|`&#188;`|`&frac14;`|Ü|`&#220;`|`&Uuml;`|ü|`&#252;`|`&uuml;`|
|½|`&#189;`|`&frac12;`|Ý|`&#221;`|`&Yacute;`|ý|`&#253;`|`&yacute;`|
|¾|`&#190;`|`&frac34;`|Þ|`&#222;`|`&THORN;`|þ|`&#254;`|`&thorn;`|
|¿|`&#191;`|`&iquest;`|ß|`&#223;`|`&szlig;`|ÿ|`&#255;`|`&yuml;`|
|À|`&#192;`|`&Agrave;`|à|`&#224;`|`&agrave;`|


## 区块元素
#### <span id='dl_hh'>段落和换行</span>

在段落后面使用 <kbd>ENTER</kbd> 换行，或者使用<code>`<br>`</code>换行，

    START==========================================
    1、只有在开水里，茶叶才能展开生命浓郁的香气。'+ENTER'
    2、人生就像奔腾的江水，没有岛屿与暗礁，就难以激起美丽的浪花。'+2*ENTER'
    3、别人能做到的事，我一定也能做到。'+*ENTER'
    4、不要浪费你的生命，在你一定会后悔的地方上。'+<br>'
    5、逆境中，力挽狂澜使强者更强，随波逐流使弱者更弱。'+2*<br>'
    6、凉风把枫叶吹红，冷言让强者成熟。'+*<br>'
    END  ==========================================
START==========================================
1、只有在开水里，茶叶才能展开生命浓郁的香气。

2、人生就像奔腾的江水，没有岛屿与暗礁，就难以激起美丽的浪花。


3、别人能做到的事，我一定也能做到。





4、不要浪费你的生命，在你一定会后悔的地方上。<br>
5、逆境中，力挽狂澜使强者更强，随波逐流使弱者更弱。<br><br>
6、凉风把枫叶吹红，冷言让强者成熟。<br><br><br><br>
END  ==========================================

#### <span id='title_ele'>标题</span>

类 Setext 形式是用底线的形式，利用 = （最高阶标题）和 - （第二阶标题），例如：

    '#'·美好大世界
    =============
    '##'·原来的未来
    -------------
任何数量的 = 和 - 都可以有效果。

'#'·美好大世界
=============
'##'·原来的未来
-------------

类 Atx 形式则是在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶，例如：

    # 'H1 一级标题'

    ## 'H2 二级标题'

    ###### 'H6 六级标题'

# H1 一级标题
## H2 二级标题
###### H6 六级标题

你可以选择性地「闭合」类 atx 样式的标题，这纯粹只是美观用的，若是觉得这样看起来比较舒适，你就可以在行尾加上 #，而行尾的 # 数量也不用和开头一样（行首的井字符数量决定标题的阶数）：


    # 'H1 一级标题' #

    ## 'H2 二级标题' ##

    ### 'H3 三级标题' ######

# H1 一级标题 #
## H2 二级标题 ##
### H3 三级标题 ######

#### <span id='bq_ele'>区块引用 Blockquotes</span>

Markdown 标记区块引用是使用类似 email 中用` > `的引用方式。如果你还熟悉在 email 信件中的引言部分，你就知道怎么在 Markdown 文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上` > `：

    >'世界上一成不变的东西，只有“任何事物都是在不断变化的”这条真理。 —— 斯里兰卡'
    >'过放荡不羁的生活，容易得像顺水推舟，但是要结识良朋益友，却难如登天。 —— 巴尔扎克'
    >'这世界要是没有爱情，它在我们心中还会有什么意义！这就如一盏没有亮光的走马灯。 —— 歌德'
    >'生活有度，人生添寿。 —— 书摘'

>世界上一成不变的东西，只有“任何事物都是在不断变化的”这条真理。 —— 斯里兰卡
>过放荡不羁的生活，容易得像顺水推舟，但是要结识良朋益友，却难如登天。 —— 巴尔扎克
>这世界要是没有爱情，它在我们心中还会有什么意义！这就如一盏没有亮光的走马灯。 —— 歌德
>生活有度，人生添寿。 —— 书摘

Markdown 也允许偷懒只在整个段落的第一行最前面加上` > `：

    >'世界上一成不变的东西，只有“任何事物都是在不断变化的”这条真理。 —— 斯里兰卡'
     '过放荡不羁的生活，容易得像顺水推舟，但是要结识良朋益友，却难如登天。 —— 巴尔扎克'
     '这世界要是没有爱情，它在我们心中还会有什么意义！这就如一盏没有亮光的走马灯。 —— 歌德'
     '生活有度，人生添寿。 —— 书摘'

>世界上一成不变的东西，只有“任何事物都是在不断变化的”这条真理。 —— 斯里兰卡
过放荡不羁的生活，容易得像顺水推舟，但是要结识良朋益友，却难如登天。 —— 巴尔扎克
这世界要是没有爱情，它在我们心中还会有什么意义！这就如一盏没有亮光的走马灯。 —— 歌德
生活有度，人生添寿。 —— 书摘

区块引用可以嵌套（例如：引用内的引用），只要根据层次加上不同数量的 > ：

    >'1.你若要喜爱你自己的价值，你就得给世界创造价值。     ——歌德'
    >>'2.人生不是一种享乐，而是一桩十分沉重的工作。    ——列夫·托尔斯泰'
    >>>'3.人生的价值，并不是用时间，而是用深度去衡量的。   ——列夫·托尔斯泰'
    >>>>'4.一个人的价值，应该看他贡献什么，而不应当看他取得什么。   ——爱因斯坦'
    >'5.人只有献身于社会，才能找出那短暂而有风险的生命的意义。   ——爱因斯坦'
    >>'6.芸芸众生，孰不爱生？爱生之极，进而爱群。    ——秋瑾'

>1.你若要喜爱你自己的价值，你就得给世界创造价值。     ——歌德
>>2.人生不是一种享乐，而是一桩十分沉重的工作。    ——列夫·托尔斯泰
>>>3.人生的价值，并不是用时间，而是用深度去衡量的。   ——列夫·托尔斯泰
>>>>4.一个人的价值，应该看他贡献什么，而不应当看他取得什么。   ——爱因斯坦

>5.人只有献身于社会，才能找出那短暂而有风险的生命的意义。   ——爱因斯坦

>>6.芸芸众生，孰不爱生？爱生之极，进而爱群。    ——秋瑾

引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等：

    > ## 这是一个标题。
    > 
    > 1.   有序列表第一条-干。
    > 2.   有序列表第二条-使劲干。
    > 
    > 给出一些例子代码：
    > 
    >     ``` perl
    >     function showMsg(){
    >       console.log('javascript say: I'm very fine!');
    >     }
    >     
    >     ```

> ## 这是一个标题。
> 
> 1.   有序列表第一条-干。
> 2.   有序列表第二条-使劲干。
> 
> 给出一些例子代码：
> 
>     ``` perl
>     function showMsg(){
>       console.log('javascript say: I'm very fine!');
>     }
>     
>     ```

#### <span id='list_ele'>列表</span>

Markdown 支持有序列表和无序列表。
无序列表使用星号、加号或是减号作为列表标记：

    -   Red
    -   Green
    -   Blue
    等同于：
    *   Red
    *   Green
    *   Blue
    也等同于：
    +   Red
    +   Green
    +   Blue

-   Red
-   Green
-   Blue
等同于：
*   Red
*   Green
*   Blue
也等同于：
+   Red
+   Green
+   Blue

有序列表则使用数字接着一个英文句点：

    1.  Bird
    2.  McHale
    3.  Parish

1.  Bird
2.  McHale
3.  Parish

很重要的一点是，你在列表标记上使用的数字并不会影响输出的 HTML 结果：

    1.  笑脸
    1.  哭脸
    1.  So Happy

    或甚至是：

    3. 乱来
    1. 乱搞
    8. 不怕事


1.  笑脸
1.  哭脸
1.  So Happy

或甚至是：

3. 乱来
1. 乱搞
8. 不怕事

列表项目标记通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面则一定要接着至少一个空格或制表符。

要让列表看起来更漂亮，你可以把内容用固定的缩进整理好：

       *   紫霞离开至尊宝后
        至尊宝才能真正成长为孙悟空 
    *   伊泽：我们是一夜情？ 
        余飞：把情删了。 
        伊泽：我们是性爱伴侣啊？ 
        余飞：把爱删了。

   *   紫霞离开至尊宝后
    至尊宝才能真正成长为孙悟空 
*   伊泽：我们是一夜情？ 
    余飞：把情删了。 
    伊泽：我们是性爱伴侣啊？ 
    余飞：把爱删了。

但是如果你懒，那也行：

    *   紫霞离开至尊宝后
    至尊宝才能真正成长为孙悟空 
    *   伊泽：我们是一夜情？ 
    余飞：把情删了。 
    伊泽：我们是性爱伴侣啊？ 
    余飞：把爱删了。

*   紫霞离开至尊宝后
至尊宝才能真正成长为孙悟空 
*   伊泽：我们是一夜情？ 
余飞：把情删了。 
伊泽：我们是性爱伴侣啊？ 
余飞：把爱删了。

如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 <p> 标签包起来，举例来说：

    *   ONE
    *   TOW
    带换行
    *   ONE

    *   TOW

*   ONE
*   TOW

带换行

*   ONE

*   TOW

列表项目可以包含多个段落，每个项目下的段落都必须缩进 4 个空格或是 1 个制表符：

    1.  This is a list item with two paragraphs. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit. Aliquam hendrerit
        mi posuere lectus.

        Vestibulum enim wisi, viverra nec, fringilla in, laoreet
        vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
        sit amet velit.

    2.  Suspendisse id sem consectetuer libero luctus adipiscing.

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

如果你每行都有缩进，看起来会看好很多，当然，再次地，如果你很懒惰，Markdown 也允许：

    1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

        Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

    2.  Suspendisse id sem consectetuer libero luctus adipiscing.

1.  This is a list item with two paragraphs. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit. Aliquam hendrerit
mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

如果要在列表项目内放进引用，那` > `就需要缩进：

    *   A list item with a blockquote:
    
        > This is a blockquote
        > inside a list item.

*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.

如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 2 个制表符：

    *   一列表项包含一个列表区块：
    
            "<代码写在这>"
            class EveryDay{
            private String message;
    
                public EveryDay(){
                    System.out.println("every day I'm busy!");
                    }
            }

*   一列表项包含一个列表区块：

        "<代码写在这>"
        class EveryDay{
        private String message;

            public EveryDay(){
                System.out.println("every day I'm busy!");
                }
        }

当然，项目列表很可能会不小心产生，像是下面这样的写法：

    2018. This year is change.

2018. This year is change.

换句话说，也就是在行首出现数字-句点-空白，要避免这样的状况，你可以在句点前面加上反斜杠。

    2018\. This year is change.

2018\. This year is change.

#### <span id='code_ele'>代码区块</span>

和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用 `<pre>` 和 `<code>` 标签来把代码区块包起来。

要在 Markdown 中建立代码区块很简单，只要简单地缩进 4 个空格或是 1 个制表符就可以，例如，下面的输入：

    这是一个普通段落：

        这是一个代码区块。

效果：

这是一个普通段落：

    这是一个代码区块

一个代码区块会一直持续到没有缩进的那一行（或是文件结尾）。

    Here is an example of AppleScript:start

        tell application "Foo"
            beep
        end tell
    Here is an example of AppleScript: end

效果：

Here is an example of AppleScript:start

    tell application "Foo"
        beep
    end tell
Here is an example of AppleScript: end

Tab缩进 4 个空格或是 1 个制表符 可以代码显示

        <div class="footer">
            &copy; 2018 FFEWI Corporation
        </div>

效果：

    <div class="footer">
        &copy; 2018 FFEWI Corporation
    </div>

#### <span id='cutLine_ele'>分隔线</span>

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

    * * *

    ***

    *****

    - - -

    _ _ _

效果：

* * *

***

*****

- - -

_ _ _

## 区段元素
#### <span id='linkUrl_ele'>链接</span>

Markdown 支持两种形式的链接语法： 行内式和参考式两种形式。
不管是哪一种，链接文字都是用 [方括号] 来标记。
要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：

    This is [an example](http://ffewi.com/ "Title") inline link.

    [This link](http://ffewi.com/) has no title attribute.

This is [an example](http://ffewi.com/ "Title") inline link.

[This link](http://ffewi.com/) has no title attribute.

如果当前域名链接的资源，可以使用相对路径：

    See my [About](#dl_hh) page for details.

See my [About](#dl_hh) page for details.

参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：

    This is [an example][id] reference-style link.
    [id]: http://ffewi.com/  "Optional Title Here"

This is [an example][id] reference-style link.
[id]: http://ffewi.com/  "Optional Title Here"

链接内容定义的形式为：

方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字

*   接着一个冒号
*   接着一个以上的空格或制表符
*   接着链接的网址
*   选择性地接着 title 内容，可以用单引号、双引号或是括弧包着

下面这三种链接的定义都是相同：

    My home address is [FFEWI][link].

    [link]: http://ffewi.com/  "Optional Title Here One"
    [link]: http://ffewi.com/  'Optional Title Here Two'
    [link]: http://ffewi.com/  (Optional Title Here Three)

My home address is [FFEWI][link].
[link]: http://ffewi.com/  "Optional Title Here One"
[link]: http://ffewi.com/  'Optional Title Here Two'
[link]: http://ffewi.com/  (Optional Title Here Three)

链接网址也可以用方括号包起来：
    
    [id]: <http://ffewi.com/>  "Optional Title Here"

你也可以把 title 属性放到下一行，也可以加一些缩进，若网址太长的话，这样会比较好看：

    [view the url title][id]
    [id]: http://ffewi.com
        "Optional Title Here Is My Title"

[view the url title][id]
[id]: http://ffewi.com
    "Optional Title Here Is My Title"

链接辨别标签可以有字母、数字、空白和标点符号，但是并不区分大小写，因此下面两个链接是一样的：

    [link text][a]
    [link text][A]

隐式链接标记功能让你可以省略指定链接标记，这种情形下，链接标记会视为等同于链接文字，要用隐式链接标记只要在链接文字后面加上一个空的方括号，如果你要让 "Google" 链接到 google.com，你可以简化成：

    [Google][]
然后定义链接内容：

    [Google]: http://google.com/

[Google][]
[Google]: http://google.com/

由于链接文字可能包含空白，所以这种简化型的标记内也允许包含多个单词：

    Visit [ffewi's blog][] for more information.

 然后接着定义链接：

    [ffewi's blog]: http://ffewi.com/   

Visit [ffewi's blog][] for more information.
[ffewi's blog]: http://ffewi.com/


链接的定义可以放在文件中的任何一个地方，我比较偏好直接放在链接出现段落的后面，你也可以把它放在文件最后面，就像是注解一样。

下面是一个参考式链接的范例：

     'I get 10 times more traffic from [Google] [1] than from [Yahoo] [2] or [MSN] [3].'
      [1]: http://google.com/        "Google"
      [2]: http://search.yahoo.com/  "Yahoo Search"
      [3]: http://search.msn.com/    "MSN Search"

I get 10 times more traffic from [Google] [1] than from [Yahoo] [2] or [MSN] [3].
  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"

同样可以改成用链接名称的方式写：

    I get 10 times more traffic from [Google][] than from [Yahoo][] or [MSN][].

      [google]: http://google.com/        "Google"
      [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
      [msn]:    http://search.msn.com/    "MSN Search"

I get 10 times more traffic from [Google][] than from [Yahoo][] or [MSN][].
  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"

同样可以改成用行内式的方式写： 

    I get 10 times more traffic from [Google](http://google.com/ "Google") than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or [MSN](http://search.msn.com/ "MSN Search").

I get 10 times more traffic from [Google](http://google.com/ "Google") than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or [MSN](http://search.msn.com/ "MSN Search").

#### <span id='strong_ele'>强调</span>

Markdown 使用星号（*）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 ` <em> ` 标签包围，用两个 * 或 _ 包起来的话，则会被转成 ` <strong> `，例如：

    *single asterisks*
    _single underscores_
    **double asterisks**
    __double underscores__

*single asterisks*
_single underscores_
**double asterisks**
__double underscores__

你可以随便用你喜欢的样式，唯一的限制是，你用什么符号开启标签，就要用什么符号结束。
强调也可以直接插在文字中间：

    'un*frigging*believable'

un*frigging*believable

但是如果你的 * 和 _ 两边都有空白的话，它们就只会被当成普通的符号。
如果要在文字前后直接插入普通的星号或底线，你可以用反斜线：
    
    \*this text is surrounded by literal asterisks\*

\*this text is surrounded by literal asterisks\*

#### <span id='codeSource_ele'>代码</span>

如果要标记一小段行内代码，你可以用反引号把它包起来（<code> ` </code>），例如：

    Use the `printf()` function.

Use the `printf()` function.

如果要在代码区段内插入反引号，你可以用多个反引号来开启和结束代码区段：

    ``There is a literal backtick (`) here.``

``There is a literal backtick (`) here.``

代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：

    A single backtick in a code span: `` ` ``

    A backtick-delimited string in a code span: `` `foo` ``

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

    Please don't use any `<blink>` tags.
    `&#8212;` is the decimal-encoded equivalent of `&mdash;`.

Please don't use any `<blink>` tags.
`&#8212;` is the decimal-encoded equivalent of `&mdash;`.

#### <span id='picture_ele'>图片</span>

很明显地，要在纯文字应用中设计一个「自然」的语法来插入图片是有一定难度的。
Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。
行内式的图片语法看起来像是：

    ![Alt text](../../pic/common/favicon.ico)
    ![Alt text](../../pic/common/favicon.ico "Optional title")

效果：
<div style="width: 100px;height: 100px;">![Alt text](../../pic/common/favicon.ico)</div>
<div style="width: 100px;height: 100px;">![Alt text](../../pic/common/favicon.ico "Optional title")</div>

详细叙述如下：

* 一个惊叹号 !
* 接着一个方括号，里面放上图片的替代文字
* 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。

参考式的图片语法则长得像这样：

    ![Alt text][id]
「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：    

    [id]: ../../pic/common/favicon.ico  "Optional title attribute"
效果：
<div style="width: 100px;height: 100px;">![Alt text][id]</div>
[id]: ../../pic/common/favicon.ico  "Optional title attribute"

如果想指定图片高宽，到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以这样使用
``` html
<div style="width: 150px;height: 150px;">
    ![Alt text](../../pic/common/favicon.ico)
</div>
```
效果：   
<div style="width: 150px;height: 150px;">![Alt text](../../pic/common/favicon.ico)</div>
还可以设置圆形

``` html
<div style="width: 100px;height: 100px; border-radius: 50%;overflow: hidden;border: solid 1px purple;">
    ![Alt text](../../pic/common/favicon.ico)
</div>
```
效果：   
<div style="width: 100px;height: 100px; border-radius: 50%;overflow: hidden;border: solid 1px #999;">![Alt text](../../pic/common/favicon.ico)</div>

## 其他
#### <span id='autoLink_ele'>自动链接</span>
Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用方括号包起来， Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样，例如：

    <http://ffewi.com/>
<http://ffewi.com/>
邮址的自动链接也很类似，只是 Markdown 会先做一个编码转换的过程，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：

    <ffewi@foxmail.com>
<ffewi@foxmail.com>

#### <span id='backslash_ele'>反斜杠</span>
Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号，例如：如果你想要用星号加在文字旁边的方式来做出强调效果（但不用 ` <em> ` 标签），你可以在星号的前面加上反斜杠：

    \*literal asterisks\*
\*literal asterisks\*

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

| 显示效果 | 转义代码 | 中文意思| 显示效果 | 转义代码 | 中文意思| 显示效果 | 转义代码 | 中文意思|
|:-----:| ------ | ----- |:-----:| ------ | ----- |:-----:| -------- | ----- |
|\ | ` \\ ` | 反斜线| \{\} | `\{\}` | 花括号|+ | `\+  ` | 加号|
|` | `` \` `` | 反引号|[]| `\[\]` | 方括号|- | `\-  ` | 减号|
|* | `\*  ` | 星号|()| `\(\)` | 括弧|. | `\.  ` | 英文句点|
|_ | `\_  ` | 底线|# | `\#  ` | 井字号|! | `\!  ` | 惊叹号|


<center>暂时总结到此，以后有新内容再附加</center>

<!-- 尾部引用 -->

<script src="./../../js/jquery.min.js"></script>
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
<link href="../../css/md_code.min.css" rel="stylesheet">
<script src="../../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->