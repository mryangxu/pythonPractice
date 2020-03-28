'''发送同时支持html 和 纯文本的邮件 收件人因为设备太古老，查看不了html的时候能自动降级，查看纯文本'''


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

import smtplib

def __format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'mryangx@163.com'
password = 'GEQFOVSRAFRERWJK'
to_addr = 'mr.yangxu@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart('alternative')

msg.attach('hello', 'plain', 'utf-8')
msg.arrach('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = __format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = __format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()