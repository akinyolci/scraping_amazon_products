import scrapy
from ..items import AmazonItem

class BotSpider(scrapy.Spider):
    name = 'bot'
    page_number = 4
    start_urls = [
        
        'https://www.amazon.com/s?i=grocery&rh=n%3A16310101&fs=true&page=5&qid=1663505602&ref=sr_pg_3',
         #for i in 400 ?
    ]

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()

        all_products_asins = response.xpath('//*[@data-asin]')

        products_asins_list = []
        for product in all_products_asins:
            asin = product.xpath('@data-asin').extract_first()
            products_asins_list.append( asin ) #product_url = f"https://www.amazon.com/dp/{asin}"






        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = products_asins_list

        yield items





















        """
        next_page = response.css('span.s-pagination-strip a::attr(href)').get()
        yield response.follow(next_page, self.parse)
        """

        """
        next_page = 'https://www.amazon.com/s?i=grocery&rh=n%3A16310101&fs=true&page='+ str(BotSpider.page_number) +'&qid=1663505602&ref=sr_pg_3'
        if BotSpider.page_number <= 7:
            BotSpider.page_number +=1
            response.follow(next_page, _Callback=self.parse)
            """
        """
        next_page = response.css('span.s-pagination-strip a::attr(href)').get()

        if next_page is not None:
            response.follow(next_page, self.parse)
         """