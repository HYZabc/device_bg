import json
from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS
import pymysql
import apis.aep_device_command
import apis.aep_device_management
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)

db = pymysql.connect(
    host="124.222.50.12",
    user="root",
    password="56206267huang",
    db="test",
    charset="utf8"
)
cur = db.cursor()


# 检索产品
@app.route('/product')
def product():
    cur.execute('select * from product')
    data = cur.fetchall()
    print(type(data), data)
    arr = []
    for i in data:
        d = {}
        d['productID'] = i[0]
        d['APIkey'] = i[1]
        d['productName'] = i[2]
        d['deviceTableName'] = i[3]
        arr.append(d)
    print(arr)
    return arr


# 获取设备
@app.route('/', methods=['POST'])
def hello_word():
    l = []
    print(request.form)
    tableName = request.form['tableName']
    print(tableName)
    cur.execute('select * from %s' % (tableName))
    data = cur.fetchall()
    # print(type(data))

    for i in data:
        dict = {}
        dict["deviceId"] = i[0]
        dict["deviceName"] = i[1]
        dict["deviceStatus"] = i[2]
        dict["createTime"] = i[3]
        dict["updateTime"] = i[4]
        dict['onlineAt'] = i[5]
        dict['offlineAt'] = i[6]
        l.append(dict)

    # print(l)
    return l


# 指令下发
@app.route('/issue', methods=['POST'])
def issue():
    print(request.form)
    data = request.form['data']
    id = request.form['id']
    key = request.form['key']
    PID = request.form['PID']
    print(data, id, key)
    result = apis.aep_device_command.CreateCommand('ZTMUWG5nQn6', 'x5oduN7gIc', key,
                                                   '{"content":{"params":{"data":"%s"},"serviceIdentifier": "xm_json_down"},"deviceId": "%s","operator": "huangyaozu","productId": %s,  "ttl": 7200, "level": 1}' % (
                                                       data, id, PID))
    d = result.decode()  # 去掉前缀b
    code = json.loads(d)  # str转dict字典
    print(type(code['msg']), code['msg'])
    if code == 'ok':
        ok = {'code': 200, "data": "指令下发成功"}
        return ok
    else:
        err = d
        return err
    # return '123'


# 单个添加设备
@app.route('/add', methods=['POST'])
def add_device():
    name = request.form['name']  # 设备名称
    sn = request.form['id']  # 设备编号
    APIKey = request.form['APIKey']  # Master-APIkey
    productID = request.form['productID']  # 产品ID
    TableName = request.form['tableName']  # 表名
    print(name, sn, APIKey, productID, TableName)
    result = apis.aep_device_management.CreateDevice('ZTMUWG5nQn6', 'x5oduN7gIc', APIKey,
                                                     '{"deviceName": "%s", "deviceSn": "%s", "operator": "huangyaozu", "productId": %s}' % (
                                                         name, sn, productID))
    d = result.decode()
    code = json.loads(d)
    print(code)
    if code['code'] == 0:
        productID = productID.replace('"', '')
        deviceID = productID + sn
        print('ZTMUWG5nQn6', 'x5oduN7gIc', APIKey, deviceID, productID)
        res = apis.aep_device_management.QueryDevice('ZTMUWG5nQn6', 'x5oduN7gIc', APIKey, deviceID, int(productID))
        de = res.decode()
        code1 = json.loads(de)
        print("code1:",code1)
        if 'result' in code1.keys():
            print(code1['result'])
            arr = code1['result']
            createTime_local = time.localtime(arr['createTime'] / 1000)
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", createTime_local)
            if arr['updateTime'] == None:
                updateTime = createTime
            else:
                updateTime_local = time.localtime(arr['updateTime'] / 1000)
                updateTime = time.strftime("%Y-%m-%d %H:%M:%S", updateTime_local)
            sql = f'insert into {TableName}(deviceId, deviceName, deviceStatus, createTime, updateTime) values(%s, %s, %s, %s, %s) '
            values = (arr['deviceId'], arr['deviceName'], arr['deviceStatus'], createTime, updateTime)
            cur.execute(sql, values)
            db.commit()
    return code
    # return 'add'


# 删除单个设备
@app.route('/delete', methods=['POST'])
def delete_device():
    print(request.form)
    APIKey = request.form['APIkey']
    productID = request.form['productID']
    deviceID = request.form['deviceID']
    TableName = request.form['tableName']
    print(APIKey, productID, deviceID)
    result = apis.aep_device_management.DeleteDevice('ZTMUWG5nQn6', 'x5oduN7gIc', APIKey, int(productID), deviceID)
    d = result.decode()
    code = json.loads(d)
    print(code)
    if code['code'] == 0:
        l = []
        sql = f'delete from {TableName} where deviceID={deviceID}'
        cur.execute(sql)
        cur.execute(f'select * from {TableName}')
        data = cur.fetchall()
        print(data)
        for i in data:
            dict = {}
            dict["deviceId"] = i[0]
            dict["deviceName"] = i[1]
            dict["deviceStatus"] = i[2]
            dict["createTime"] = i[3]
            dict["updateTime"] = i[4]
            dict['onlineAt'] = i[5]
            dict['offlineAt'] = i[6]
            l.append(dict)
        db.commit()
    code['data'] = l
    return code
    # return 'delete'


if __name__ == '__main__':
    app.run('0.0.0.0', '5555')
