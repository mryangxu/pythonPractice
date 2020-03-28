from email.mime.text import MIMEText

# 构建纯文本邮件
msg = MIMEText('hello', 'plain', 'utf-8')

from_addr = input('From:') # 发件人地址
password = input('Password:') # 密码
to_addr = input('To:') # 收件人
smtp_server = input('SMTP server:') # SMTP服务地址

import smtplib

server = smtplib.SMTP(smtp_server, 25) # 创建发送邮件的服务
server.set_debuglevel(1) # 打印交互信息
server.login(from_addr, password) # 登陆SMTP服务器

server.sendmail(from_addr, [to_addr], msg.as_string()) # 发送邮件

server.quit()

