# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class StackoverflowItem(scrapy.Item):
    # 链接
    links = scrapy.Field()
    # 查看次数
    views = scrapy.Field()
    # 票数
    votes = scrapy.Field()
    # 回答数
    answers = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 问题
    questions = scrapy.Field()
