import zmail

class ZMailObject(object):

    def __init__(self, username, authorization_code ):
        # 邮箱账号
        self.username = username

        # 邮箱授权码
        self.authorization_code = authorization_code

        # 构建一个邮箱服务对象
        self.server = zmail.server(self.username, self.authorization_code)

# 邮件主体
mail_body = {
        'subject': '测试报告',
        'content_text': '这是一个测试报告',  # 纯文本或者HTML内容
        #'attachments': ['/home/atguigu/crontab/Mail.py'],
}

# 发件人
mail_to_list = [
    "yuanxin9997@qq.com",
    "2544939647@qq.com"
]

# 发送邮箱
zmailobj = ZMailObject("yuanxin9997@163.com", "IBJLBPTQHHDHXMEY")
zmailobj.server.send_mail(mail_to_list, mail_body)
print("Done")