from report.html_report import html_report
from emailfile import send_email
from pagebase import conf
from pagebase.runlog import RunLog

# 执行测试，并输出测试报告
test_report = html_report()
test_report.make_report()

# 发送邮件,可在配置文件中修改email_conf ，来决定是否发送邮件，默认0为发送
em_conf = conf.MessageIni()
em_config = em_conf.email_message()
log = RunLog()
if em_config[4] == "0":
    send_email_report = send_email.SendEmail()
    send_email_report.send()
    print("邮件发送完成")
    log.logInfo()

else:
    print("无需发送邮件")
    log.logInfo()















