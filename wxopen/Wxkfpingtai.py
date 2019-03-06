# -*- coding: utf-8 -*-
import wxopen.httpCurl as httcurl
#发送模板消息
class Wxkfpingtai:
    def sendTemplate(access_token,data):
        url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token='+access_token
        http_curl = httcurl.httpCurl()
        return http_curl.curls(url,data,'POST')
