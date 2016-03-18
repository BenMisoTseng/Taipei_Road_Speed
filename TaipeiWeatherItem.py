# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaipeiWeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tempC = scrapy.Field()
    tempF = scrapy.Field()
    weather = scrapy.Field()
    windDir = scrapy.Field()
    wind = scrapy.Field()
    gustwind = scrapy.Field()
    visibility = scrapy.Field()
    relativeH = scrapy.Field()
    pressure = scrapy.Field()
    accumulatedP = scrapy.Field()