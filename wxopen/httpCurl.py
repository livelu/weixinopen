# -*- coding: utf-8 -*-
from requests import request
import json
from io import *
import time, datetime
class httpCurl:

    def curls(self,url,data = {}, method='GET'):

        res = request(method,url,json=data)
        return res
        # b = BytesIO()
        # curl = pycurl.Curl()
        # curl.setopt(pycurl.URL, url)
        # curl.setopt(pycurl.USERAGENT,
        #             "Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")  # 配置请求HTTP头的User-Agent
        # curl.setopt(pycurl.CONNECTTIMEOUT, 60)
        # curl.setopt(pycurl.TIMEOUT, 30)
        # curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        # if(method == 'POST'):
        #     curl.setopt(curl.POST, 1)  # 1表示调用post方法而不是get
        #     curl.setopt(curl.POSTFIELDS, json.dumps(data))  # 发送数据
        # curl.setopt(curl.WRITEFUNCTION, b.write)
        # curl.perform()
        # httcode = curl.getinfo(pycurl.HTTP_CODE)
        # logger.info(b.getvalue())
        # logger.info(httcode)
        # if (httcode == 200):
        #    return b.getvalue()
        # else:
        #     return b.getvalue()
        # b.close()
        # curl.close()