# -*- coding: utf-8 -*-
import curl as Curl
#发送模板消息
class Wxkfpingtai:
    def sendTemplate(self,access_token,data):
        url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token='+access_token
        httpcurl = Curl.curl()
        httpcurl.request(url,data,'POST')
