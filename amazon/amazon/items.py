# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    products_names_list = scrapy.Field()
    products_prices_list = scrapy.Field()
    products_asins_list = scrapy.Field()


    
