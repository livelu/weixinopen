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
        'form_id':'b04c4be8b4574681800ab0e070db95b1',
        'data':{
            'keyword1':{'value':'张璐'},
            'keyword2':{'value':time.strftime('%Y-%m-%d %H:%M:%S')},
            'keyword3':{'value':'python发送'},
        }
    }
res = Wxkfpingtai.sendTemplate('19_WYRxyrEXgTEQxcl1mvmDZWd6zTsi6XFuFXuAMV8zgxRxx3VrqtH37KdTZm4XMXKhVn_8dY8RD6qLLENH-Axsl_gZhioIIwPLmRQwsuINbHMdWQBwIzkHosZ3JrAYi8HTWqZ2z80C7yhaUfwUMBXiAGDFUQ',data)
#print(res)
print(res.status_code)
print(res.json())
