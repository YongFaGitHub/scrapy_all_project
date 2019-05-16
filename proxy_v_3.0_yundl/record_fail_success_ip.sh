#!/bin/bash
basedir=$(dirname $0)
cd $basedir
time=$(date -d '10 minute ago' +'%Y-%m-%d %H:%M')
((time_len=${#time}-1))
time=${time:0:$time_len}
success_flag=success
success_count=$(cat logs/proxyPool.log | grep "$time" | grep $success_flag | wc -l)
fail_flag=fail
fail_count=$(cat logs/proxyPool.log | grep "$time" | grep $fail_flag | wc -l)
time=$time'0'
python insert_into_mysql.py "$time"  $success_count $fail_count
