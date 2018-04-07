<style type="text/css">
    .markdown-body pre code{
        color:black;
    }
</style>

## 使用 supervisor 管理项目启动

> 安装 supervisor

    pip install supervisor
    echo_supervisord_conf > supervisor.conf   # 生成 supervisor 默认配置文件
    vim supervisor.conf                       # 修改 supervisor 配置文件


>配置 supervisor

    [program:MyApp]
    command= python /home/py/app/app.py    ; supervisor启动命令
    directory= /home/py/app                ; 项目的文件夹路径
    startsecs=0                            ; 启动时间
    stopwaitsecs=0                         ; 终止等待时间
    autostart=false                        ; 是否自动启动
    autorestart=false                      ; 是否自动重启
    stdout_logfile=/home/log/app.log       ; log 日志
    stderr_logfile=/home/log/app.err       ; 错误日志
    user        = root
    redirect_stderr         = true
    stdout_logfile_maxbytes = 50MB
    stdout_logfile_backups  = 10

>supervisor的基本使用命令

    supervisord -c supervisor.conf          通过配置文件启动supervisor
    supervisorctl -c supervisor.conf status 察看supervisor的状态
    supervisorctl -c supervisor.conf reload 重新载入 配置文件
    supervisorctl -c supervisor.conf start [all]|[appname]  启动指定/所有 supervisor管理的程序进程
    supervisorctl -c supervisor.conf stop [all]|[appname]   关闭指定/所有 supervisor管理的程序进程


<!-- md文档区域 END -->

<!-- 代码高亮 -->
<link href="../css/md_code.min.css" rel="stylesheet">
<script src="../js/highlight.min.js"></script>
<script >hljs.initHighlightingOnLoad();</script>  
<!-- 代码高亮结束 -->