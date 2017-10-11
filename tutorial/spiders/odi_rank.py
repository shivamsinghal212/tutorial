import scrapy


class cricSpider(scrapy.Spider):
	name = "odi_rank"
	start_urls = ['http://www.cricbuzz.com/cricket-stats/icc-rankings/batsmen-rankings']
	

	def parse(self, response):
		for i in range(2,101):
			item={
			'Position':response.xpath('//*[@id="batsmen-odis"]/div[$val]/div[1]/text()',val=i).extract(),
			'Player':response.xpath('//*[@id="batsmen-odis"]/div[$val]/div[2]/div[2]/a/text()',val=i).extract(),
			'Country':response.xpath('//*[@id="batsmen-odis"]/div[$val]/div[2]/div[2]/div/text()',val=i).extract(),
			'Rating':response.xpath('//*[@id="batsmen-odis"]/div[$val]/div[3]/text()',val=i).extract(),
			'Best_Rank':response.xpath('//*[@id="batsmen-odis"]/div[$val]/div[4]/text()',val=i).extract()
			}
			
			yield item
		return
