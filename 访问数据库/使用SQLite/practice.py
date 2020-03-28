import sqlite3

# 连接到数据库 数据库文件是test.db 如果不存在回自动在当前目录创建这个文件
conn = sqlite3.connect('test.db')

# 创建一个游标
cursor = conn.cursor()

# 执行一条sql语句 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一条数据
cursor.execute('insert into user (id, name) values(\'1\', \'李四\')')

# 获取插入结果
print(cursor.rowcount)

# 关闭游标
cursor.close()

# 提交事务
conn.commit()

# 关闭数据库连接
conn.close()