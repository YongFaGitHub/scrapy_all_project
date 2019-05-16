# ProxyPool
Crawl and validate proxies from Internet
# Requirement
```
requests
gevent
lxml
beautifulsoup4
```
# How to use
just run in terminal
```
python proxypool.py
#启动线程池，验证ip有效
```
then
```
http://localhost:8080
```
or
```
http://localhost:8080/?num=1&port=80&type=3&protocol=http&area=北京
```
# Other
```
the parameter "type" means anonymous level
0: unknown
1: transparent
2: anonymous
3: high anonymous
```
# Note
1. 程序自动已守护进程方式运行
2. 运行日志会重定向到logs文件中，系统日志会定向到/tmp中