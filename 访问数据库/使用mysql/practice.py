import mysql.connector

# 连接数据库 并选择test库
conn = mysql.connector.connect(user='root', password='root', database='test')

# 创建游标
cursor = conn.cursor()


# 表如果存在就删除
cursor.execute('drop table if exists user')

# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入语句
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

# 获取影响的行数
cursor.rowcount

# 提交事务
conn.commit()

# 关闭游标
cursor.close()

# 运行查询

# 建立游标
cursor = conn.cursor()

# 执行查询
cursor.execute('select * from user where id = %s', ('1',))

# 获取查询结果
value = cursor.fetchall()

print(value)

# 关闭游标
cursor.close

# 关闭连接
conn.close()