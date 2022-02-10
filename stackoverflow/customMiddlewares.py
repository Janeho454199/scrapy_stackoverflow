# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   开发人员：janeho
   开发日期：2022-02-10
   开发工具：PyCharm
   功能描述：下载中间件
-------------------------------------------------
    Change Activity:

-------------------------------------------------
"""
from stackoverflow.utils.UserAgent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class CustomUserAgent(UserAgentMiddleware):

    def __init__(self, user_agent='Scrapy'):
        super().__init__()
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = UserAgent().get_header()
        request.headers.setdefault('User-Agent', ua)
        request.headers.setdefault('Referer', 'https://stackoverflow.com')
