# -*- coding: utf-8 -*-
import platform
import os
from daemon import daemonize
from proxypool import ProxyPool

if __name__ == '__main__':
    # 以守护进程方式运行
    if "Linux" in platform.system():
         daemonize(os.getcwd(), '/dev/null','/tmp/daemon_stdout.log','/tmp/daemon_error.log')
    redis_key_https = "merge_https_proxy"
    redis_key_http = "merge_http_proxy"
    redis_distinct_set_http = "merge_set_http"
    redis_distinct_set_https = "merge_set_https"
    ProxyPool(redis_key_http=redis_key_http,
              redis_key_https=redis_key_https,
              redis_distinct_set_http=redis_distinct_set_http,
              redis_distinct_set_https=redis_distinct_set_https).run()

