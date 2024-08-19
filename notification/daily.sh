#!/bin/bash

# 待执行的命令
command_to_run="ntp"

# 判断当前时间是否为13点
while true
do
sudo ntpdate ntp.aliyun.com
current_hour=$(date +'%H')
if [ $current_hour -eq 14 ]; then
    # 执行指定命令
    dos2unix /home/atguigu/crontab/notification/*.py
    chmod +x /home/atguigu/crontab/notification/*.py
    python3 /home/atguigu/crontab/notification/main.py >> /home/atguigu/crontab/notification/notification.log 2>&1
else
    date >> /home/atguigu/crontab/notification/notification.log
    sleep 300
fi
done
