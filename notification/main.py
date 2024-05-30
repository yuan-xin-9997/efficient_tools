# encoding: utf-8
import datetime
from ZMailUtil import ZMailObject

print("-" * 50)
print(str(datetime.datetime.now()) + " - 程序开始运行...")
today = datetime.date.today()
print(today)
target_date = today + datetime.timedelta(days=14)
print(target_date)
print(target_date.weekday())  # 5代表星六
send_flag = False
if target_date.weekday() == 4:
    message = f"通知：今天是{today}，截止今天，铁路可买到最远日期的票是{target_date}（周五）!!!"
    send_flag = True
elif target_date.weekday() == 6:
    message = f"通知：今天是{today}，截止今天，铁路可买到最远日期的票是{target_date}（周日）!!!"
    send_flag = True
else:
    message = f"今天是{today}，截止今天，铁路可买到最远日期的票是{target_date}（星期{target_date.weekday()+1}）!!!"

if send_flag:
    print(str(datetime.datetime.now()) + " - " + message)
    # 邮件主体
    content_text = f"""
        {message}
        --------------------------------------------------------------------
        此邮件由系统自动发出，无需回复！
        发送时间：{str(datetime.datetime.now())}
    """
    mail_body = {
        'subject': message,
        'content_text': content_text,  # 纯文本或者HTML内容
        # 'attachments': ['/home/atguigu/crontab/Mail.py'],
    }

    # 发件人
    mail_to_list = [
        "yuanxin9997@qq.com",
        "2544939647@qq.com"
    ]

    # 邮件发送
    zmailobj = ZMailObject("yuanxin9997@163.com", "IBJLBPTQHHDHXMEY")
    zmailobj.send_email(mail_body, mail_to_list)

    print("Program Finished. exit...")
else:
    print(str(datetime.datetime.now()) + " - " + message)
    print("不满足发送条件，退出...")

print(str(datetime.datetime.now()) + " - 程序结束运行...")
