'''发送带收件人发件人备注等信息'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def __format_addr(s):
    name, addr = parseaddr(s)
    print(name, addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'mryangx@163.com'
password = 'GEQFOVSRAFRERWJK'
to_addr = 'mr.yangxu@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
msg['From'] = __format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = __format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()