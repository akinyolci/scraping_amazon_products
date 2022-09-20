from urllib.parse import urljoin
import scrapy
from ..items import AmazonItem

class BotSpider(scrapy.Spider):
    name = 'bot'
    page_number = 4
    start_urls = [
        
        'https://www.amazon.com/s?i=grocery&rh=n%3A16310101&fs=true&page=5&qid=1663505602&ref=sr_pg_3',
         #for i in 400 ?
    ]

    




    def parse_product_page(self, response):
        asin = response.meta['asin']
        title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        
        seller_rank = response.xpath('//*[text()="Amazon Best Sellers Rank:"]/parent::*//text()[not(parent::style)]').extract()
        yield {'asin': asin, 'Title': title,'SellerRank': seller_rank}



    def parse(self, response):
        items = AmazonItem()

        products_names = response.css('.a-size-base-plus::text').extract()
        products_prices = response.css('.a-price-whole').css('::text').extract()
        all_products_asins = response.xpath('//*[@data-asin]')

        products_names_list =[]
        products_prices_list = []
        products_asins_list = []

        for product in all_products_asins:
            asin = product.xpath('@data-asin').extract_first()
            if asin !="":
                products_asins_list.append( asin ) #product_url = f"https://www.amazon.com/dp/{asin}"

        for name in products_names:
            if len(name) > 2:
                products_names_list.append(name)
            
        for price in products_prices:
            if price !='.':
                products_prices_list.append(price)

        

        for asin in products_asins_list:
            product_url = f"https://www.amazon.com/dp/{asin}"
            yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})
        
        next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
        if next_page:
            url = urljoin("https://www.amazon.com",next_page)
            yield scrapy.Request(url=product_url, callback=self.parse_keyword_response)


    def parse_keyword_response(self, response):
        for asin in products_asins_list:
            product_url = f"https://www.amazon.com/dp/{asin}"
            yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})










        """
        Storage = {}
        
        counter = 0
        while counter <= len(all_products_asins):
            Storage[all_products_asins[counter]] = products_prices_list[counter]
            counter +=1
        """
        """
        for i in range(0,len(all_products_asins)):
            Storage[str(products_asins_list[i])] = str(products_prices_list[i])
        """

        items['products_names_list'] = products_names_list
        items['products_prices_list'] = products_prices_list
        items['products_asins_list'] = products_asins_list

        yield  items

        




















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