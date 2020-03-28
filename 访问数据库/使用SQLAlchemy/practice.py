from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

'''在数据库的表中添加一条数据'''

# 创建session对象
session = DBSession()

# 创建新user对象
new_user = User(id='5', name='Bob')

# 添加到session
# session.add(new_user)

# 提交（保存到数据库）
# session.commit()

# 关闭session
session.close()

# 创建Session
session = DBSession()
user = session.query(User).filter(User.id=='5').one()

print('type', type(user))
print('name', user.name)

session.close()

