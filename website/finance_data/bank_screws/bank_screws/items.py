# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from website.finance import models
from scrapy_djangoitem import DjangoItem


class BankScrewsItem(DjangoItem):  # scrapy.Item
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = models.IndexValuation  # 注入django项目的固定写法，必须起名为django_model=django中models.IndexValuation表
    pass
