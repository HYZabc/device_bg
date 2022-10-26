#!/usr/bin/python
# encoding=utf-8
import json
import re
import sys
import time

import pymysql

sys.path.append('..')
import apis.aep_device_management

db = pymysql.connect(
    host="124.222.50.12",
    user="root",
    password="56206267huang",
    db="test",
    charset="utf8"
)

cur = db.cursor()

# 根据产品id和APIKey获取设备
if __name__ == '__main__':
    result = apis.aep_device_management.QueryDeviceList('ZTMUWG5nQn6', 'x5oduN7gIc', '98de759aeed94b49a48ae6b90a7c1c01',
                                                        15341250, searchValue='', pageSize='', pageNow='')
    # result = apis.aep_device_management.QueryDeviceList('MbKMCM82GCi', '5gCsc4hD4j', '7b66b5d324c14596af94efcdf06ba1ba',
    #                                                     15153726, searchValue='', pageSize='', pageNow='')
    s = result.decode('utf-8')
    json = json.loads(s)
    print(json)
    if 'result' in json.keys():
        device_arr = json['result']['list']
        for arr in device_arr:
            # print(arr)

            createTime_local = time.localtime(arr['createTime'] / 1000)
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", createTime_local)
            if arr['updateTime'] == None:
                updateTime = createTime
            else:
                updateTime_local = time.localtime(arr['updateTime'] / 1000)
                updateTime = time.strftime("%Y-%m-%d %H:%M:%S", updateTime_local)

            if arr['onlineAt'] ==None:
                onlineAt = None
            else:
                onlineAt_local = time.localtime(arr['onlineAt'] / 1000)
                onlineAt = time.strftime("%Y-%m-%d %H:%M:%S", onlineAt_local)

            if arr['offlineAt']== None:
                offlineAt = None
            else:
                offlineAt_local = time.localtime(arr['offlineAt'] / 1000)
                offlineAt = time.strftime("%Y-%m-%d %H:%M:%S", offlineAt_local)

            # print(arr['deviceId'],  arr['deviceName'],  arr['deviceStatus'], createTime, updateTime)
            sql = 'insert into device_turbidity(deviceId, deviceName, deviceStatus, createTime, updateTime,onlineAt,offlineAt) values(%s, %s, %s, %s, %s,%s,%s) '
            values = (arr['deviceId'],  arr['deviceName'],  arr['deviceStatus'], createTime, updateTime,onlineAt,offlineAt)
            cur.execute(sql, values)
            db.commit()
            # 关闭数据库连接
            # db.close()

            # cur.execute("select * from device_management")
            # data = cur.fetchall()
            # print(data)
