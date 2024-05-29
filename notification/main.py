# encoding: utf-8
import datetime
from Mail import ZMailObject

today = datetime.date.today()
print(today)
target_date = today + datetime.timedelta(days=14)
print(target_date)
print(target_date.weekday())  # 5代表星六
send_flag = False
message = ""
if target_date.weekday() == 4:
    message = f"今天是{today}，截止今天，铁路可买到最远日期的票是{target_date}（周五）！！！"
    send_flag = True
elif target_date.weekday() == 6:
    message = f"今天是{today}，截止今天，铁路可买到最远日期的票是{target_date}（周日）！！！"
    send_flag = True
print(datetime.datetime.now() + message)


if send_flag:
    # 邮件主体
    mail_body = {
        'subject': message,
        'content_text': '如标题所示',  # 纯文本或者HTML内容
        # 'attachments': ['/home/atguigu/crontab/Mail.py'],
    }

    # 发件人
    mail_to_list = [
        "yuanxin9997@qq.com",
        "2544939647@qq.com"
    ]

    zmailobj = ZMailObject("yuanxin9997@163.com", "IBJLBPTQHHDHXMEY")
    zmailobj.server.send_mail(mail_to_list, mail_body)

    print("Done")
