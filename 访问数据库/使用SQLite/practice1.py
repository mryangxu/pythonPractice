import os, sqlite3

try:
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
except BaseException as e:
    print(e)
finally:
    cursor.close()
    conn.commit()
    conn.close()

def get_score_in(low, high):
    '返回指定区间的名字， 分数从低到高'
    try:
        print(db_file)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        info = cursor.execute('select name from user where score >=? and score <=? order by score', (low, high))
        # print(info.fetchall())

        # for x in info.fetchall():
        #     print(x[0])
        return [x[0] for x in info.fetchall()]
    except BaseException as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


# get_score_in(1, 100)
# 测试
assert get_score_in(90, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')