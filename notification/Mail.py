# encoding: utf-8
import zmail
import datetime

class ZMailObject(object):

    def __init__(self, username, authorization_code ):
        # 邮箱账号
        self.username = username

        # 邮箱授权码
        self.authorization_code = authorization_code

        # 构建一个邮箱服务对象
        self.server = zmail.server(self.username, self.authorization_code)

    def send_email(self, mail_body, mail_to_list):
        print(datetime.datetime.now() + " - email is sending")
        for rec in mail_to_list:
            self.server.send_mail(rec, mail_body)
        print(datetime.datetime.now() + " - email is sent!")
