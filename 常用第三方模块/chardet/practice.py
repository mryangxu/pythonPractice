import chardet

print(chardet.detect(b'Hello, world!'))


data = '离离原上草，一岁一枯荣'
print(chardet.detect(data.encode('gbk')))
print(chardet.detect(data.encode('utf-8')))


print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))

print(chardet.detect('の主要ニュース'.encode('euc-jp')))