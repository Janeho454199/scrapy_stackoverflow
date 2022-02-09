#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import scrapy
from stackoverflow.items import StackoverflowItem


formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('monitor')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"

    def __init__(self):
        self.count = 1

    def start_requests(self):
        _url = 'https://stackoverflow.com/questions?tab=votes&page={page}'
        urls = [_url.format(page=page) for page in range(1, 5)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for index in range(1, 51):
            self.count += 1
            if self.count % 100 == 0:
                logger.info(self.count)

            sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
            item = StackoverflowItem()
            item['votes'] = "".join(sel.xpath(
                'div[1]/div[1]/span[1]/text()').extract())
            item['answers'] = "".join(sel.xpath(
                'div[1]/div[2]/span[1]/text()').extract())
            item['views'] = "".join(
                sel.xpath('div[1]/div[3]/span[1]/text()').extract()).split()[0].replace(",", "")
            item['questions'] = "".join(sel.xpath('div[2]/div[1]/a/text()').extract())
            item['links'] = "".join(sel.xpath('div[2]/div[1]/a/@href').extract())
            item['tags'] = ",".join(sel.xpath('div[2]/div[3]/div[1]/a/text()').extract())

            yield item
