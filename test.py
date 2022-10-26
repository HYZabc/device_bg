# import pymysql
# conn = pymysql.connect(
#     host='124.222.50.12',
#     user='root',
#     password='56206267huang',
#     db='test',
#     charset='utf8',
#        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
# )
# cursor = conn.cursor()
# cursor.execute("insert into user(username,password) values('dasdasd',546515)")
# conn.commit()
# cursor.execute("select * from user")
# data = cursor.fetchall()
# print(data)

import sys
sys.path.append('..')
import apis.aep_device_management

if __name__ == '__mian__':
    result = apis.aep_device_management.QueryDeviceList('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', '1529484530')
    print('result='+str(result))