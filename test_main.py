from report.html_report import html_report
from emailfile import send_email

test_report = html_report()
test_report.make_report()

a = send_email.SendEmail()
a.send()















