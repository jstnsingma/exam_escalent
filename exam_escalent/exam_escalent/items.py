# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ExamEscalentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PbaTeamItem(scrapy.Item):
    name = scrapy.Field()
    coach = scrapy.Field()
    manager = scrapy.Field()
    url = scrapy.Field()
    logo = scrapy.Field()
    # players_info = scrapy.Field()

class PbaPlayersItem(scrapy.Item):
    name = scrapy.Field()
    team = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()
    position = scrapy.Field()
    mugshot = scrapy.Field()