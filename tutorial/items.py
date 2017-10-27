# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Position = scrapy.Field()
    Player = scrapy.Field()
    Country = scrapy.Field()
    Rating = scrapy.Field()
    Best_Rank = scrapy.Field()
