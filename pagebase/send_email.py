import smtplib
from email.mime.text import MIMEText
import conf

mail_host = 'smtp.163.com'
mail_user = 'liujie1663@163.com'
mail_pass = 'RZYDZQHDIAFXPSAQ'
#邮件发送方邮箱地址
em = conf.MessageIni()
send_address = em.email_address()
sender = "liujie1663@163.com"
receivers = [send_address]


#邮件内容设置
message = MIMEText('content','plain','utf-8')
#邮件主题
message['Subject'] = '您好，您的工作证明'
#发送方信息
message['From'] = sender
#接受方信息
message['To'] = receivers[0]

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP()
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass)
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
