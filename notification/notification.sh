#!/bin/bash
# crontab -e
# 0 13 * * * /bin/bash /home/atguigu/crontab/notification/notification.sh
# 查看crontab日志
#   tail -f /var/log/cron
# 删除crontab日志
#   > /var/log/cron


sudo ntpdate ntp.aliyun.com
dos2unix /home/atguigu/crontab/notification/*.py
chmod +x /home/atguigu/crontab/notification/*.py
python3 ./main.py > notification.log 2>&1
sudo ntpdate ntp.aliyun.com