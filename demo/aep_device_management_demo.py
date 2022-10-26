#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_management

if __name__ == '__main__':
    # result = apis.aep_device_management.QueryDeviceList('MbKMCM82GCi', '5gCsc4hD4j', '7b66b5d324c14596af94efcdf06ba1ba', 15153726, searchValue='' , pageSize='', pageNow='')
    # # result = apis.aep_device_management.QueryDeviceList('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', 15294845, searchValue='' , pageSize='', pageNow='')
    # print('result='+str(result))

    result = apis.aep_device_management.QueryDevice('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', '1529484599822', 15294845)
    print('result='+str(result))

    # result = apis.aep_device_management.DeleteDevice('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', 15294845,'15294845998')
    # print('result='+str(result))

    # result = apis.aep_device_management.UpdateDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '10015488test', '{}')
    # print('result='+str(result))

    # result = apis.aep_device_management.CreateDevice('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', '{"deviceName": "test999", "deviceSn": "999", "operator": "huangyaozu", "productId": 15294845}')
    # print('result='+str(result))

    # result = apis.aep_device_management.BindDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

    # result = apis.aep_device_management.UnbindDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

    # result = apis.aep_device_management.QueryProductInfoByImei('dFI1lzE0EN2', 'xQcjrfNLvQ')
    # print('result='+str(result))

    # result = apis.aep_device_management.ListDeviceInfo('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

    # result = apis.aep_device_management.DeleteDeviceByPost('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

    # result = apis.aep_device_management.ListDeviceActiveStatus('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

