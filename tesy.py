# -*- coding: utf-8 -*-
from wxopen.Wxkfpingtai import Wxkfpingtai
import time, datetime
import json
page = '/pages/studentIndex/studentIndex?mechanism_id=' + str(45) + '&visitingCard=true&userid=' + str(
    53)
data = {
        'touser':'ox05N5V5GZaKqQ1Zy7-sP8DKX1Lo',
        'template_id':'fc-4PTEmhRCVj4WRSp-UTyBOvyvlr4snFMEtHS8h038',
        'page':page,
        'form_id':'5f578c3458614695846c73a1aa81b1d1',
        'data':{
            'keyword1':'张璐',
            'keyword2':time.strftime('%Y-%m-%d %H:%M:%S'),
            'keyword3':'pip 发送',
        }
    }
res = Wxkfpingtai.sendTemplate('19_EpajAbRpzQoIutm9QjLA9cdrQwxCdLt42xMBjEPvyJ_yZ0iGsILFAB0tsKLj0E1lPGo0Ur5UW106tfh0kvLpRxSSrYFzTzkTo_rgQHkjbfd-HaQMNBQ_ut2FO9Bib2PyAXjh8KFWuPLHrYT_OPMiAHDCDA',json.dumps(data))
print(res.status_code)
print(res.json())
#wexin.()