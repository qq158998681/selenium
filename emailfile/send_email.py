import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pagebase import conf, runlog


class SendEmail():
    def __init__(self):
        # 创建日志对象
        self.log = runlog.RunLog()

        # 邮件基本信息
        # 读取配置文件的基本信息
        a = conf.MessageIni()
        em = a.email_message()
        self.email_addressee = em[0]
        self.email_sender = em[1]
        self.email_sender_password = em[2]
        self.email_host = em[3]

    def send(self, ):
        # 邮件内容设置
        message = MIMEMultipart()
        # 邮件主题
        message['Subject'] = '您好，自动化测试已完成，请查看邮件附件获取详细信息'
        # 发送方信息
        message['From'] = self.email_sender
        # 接受方信息
        message['To'] = self.email_addressee
        # 定义邮件附件
        html_name = time.strftime("%Y-%m-%d", time.localtime()) + "测试报告"
        htmlFile = './{}.html'.format(html_name)
        htmlApart = MIMEApplication(open(htmlFile, 'rb').read())
        htmlApart.add_header('Content-Disposition', 'attachment', filename=htmlFile)
        message.attach(htmlApart)

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.email_host, 25)
            # 登录到服务器
            smtpObj.login(self.email_sender, self.email_sender_password)
            # 发送

            smtpObj.sendmail(
                self.email_sender, self.email_addressee, message.as_string())
            # 退出
            smtpObj.quit()

            # 记录日志
            self.log.logInfo("success，邮件发送成功，系统信息：")

        except smtplib.SMTPException:
            self.log.logError("发送失败")


if __name__ == "__main__":
    a = SendEmail()
    a.send()


