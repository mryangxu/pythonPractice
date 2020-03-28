'''发送附件'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
def __format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 邮件对象

from_addr = 'mryangx@163.com'
password = 'GEQFOVSRAFRERWJK'
to_addr = 'mr.yangxu@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = __format_addr('python爱好者 <%s>' % from_addr)
msg['To'] = __format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase 从本地读取图片
with open('1.png', 'rb') as f:
    # 设置附件mime和文件名
    mime = MIMEBase('image', 'png', filename='1.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()