import scrapy


class QuotesSpider(scrapy.Spider):
    name = "phones"
    start_urls = []
    for i in range(1,5):
      j = 'https://www.flipkart.com/search?page='+str(i)+'&sid=tyy%2F4io&viewType=list'
      start_urls.append(j)
    

    def parse(self, response):
        for i in range(1,20):
            yield {
            'phone':response.xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[$val]/div/a/div[2]/div[1]/div[1]/text()',val=i).extract(),
			
            'price':response.xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[$val]/div/a/div[2]/div[2]/div[1]/div/div/text()',val=i).extract()
            }
