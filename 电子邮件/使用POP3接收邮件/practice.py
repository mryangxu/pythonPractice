import poplib

email = 'mryangx@163.com'
password = 'GEQFOVSRAFRERWJK'
pop3_server = 'pop.163.com'

# 连接到pop3服务器

server = poplib.POP3(pop3_server)

# 打开调试信息
# server.set_debuglevel(1)

# 可选 打印pop3的欢迎信息
# print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat() 返回邮件数量和占用空间
print('Message: %s. Size: %s' % server.stat())

# list() 返回所有邮件的编号
resp, mails, cotets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件 索引从1号开始
index = len(mails)
resp, lines, cotets = server.retr(index)

# lines 存储了原始邮件的所有行 可以获得整个文件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 解析出邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 解析为Message对象
msg = Parser().parsestr(msg_content)

# 邮件的Subject或者Email中包含的名字都是经过编码处理后的str， 要正常显示， 就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# decode_header()返回一个list， 因为像Cc，Bcc这样的字段可能包含多个邮件地址，所以解析出来会有多个元素，以下偷懒只取了一个元素
# 文件的内容是str， 还需要编码检测， 否则， 非utf-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


'''但是这个Message对象本身可能是一个MIMEMultipart对象， 即包含嵌套的其它MIMEBase对象，
嵌套可能还不止一层。所以我们要递归打印出Message对象的层次结构'''

# indext用于缩进显示
def print_info(msg, indext=0):
    if indext == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indext, header, value))

    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indext, n))
            print('%s----------------' % '  ' * indext)
            print_info(part, indext + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indext, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indext, content_type))


print_info(msg)

# 可以根据索引号直接从服务器删除文件
# server.dele(index)

# 关闭连接
server.close()