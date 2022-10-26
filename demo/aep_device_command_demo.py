#!/usr/bin/python
# encoding=utf-8
from asyncio.windows_events import NULL
import sys
sys.path.append('..')
import aep_device_command

if __name__ == '__main__':
    result = aep_device_command.CreateCommand('ZTMUWG5nQn6', 'x5oduN7gIc', 'fd1f72b51bf84b71a00b4bbcaf1aa26d', '{"content":{"params":{"data":"getgps"},"serviceIdentifier": "xm_json_down"},"deviceId": "1529484530","operator": "huangyaozu","productId": 15294845,  "ttl": 7200, "level": 1}')
    print('result='+str(result))

    # result = apis.aep_device_command.QueryCommandList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488, '10015488test')
    # print('result='+str(result))

    # result = apis.aep_device_command.QueryCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488, '10015488test')
    # print('result='+str(result))

    # result = apis.aep_device_command.CancelCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    # print('result='+str(result))

