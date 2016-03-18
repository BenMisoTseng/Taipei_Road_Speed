import scrapy
from TaipeiRoadSpeed.items import TaipeiWeatherItem
#from scrapy.selector import HtmlXPathSelector

class TaipeiRoadSpeed(scrapy.Spider):
	name = "TaipeiWeather"
	allowed_domains = ["www.cwb.gov.tw"]
	start_urls = ["http://www.cwb.gov.tw/V7/observe/24real/Data/46692.htm"]
	
	def parse(self, response):
		#hxs = HtmlXpathSelector(response)
		weathertime = response.xpath("//table/tr[2]/th/text()").extract()
		print weathertime
		for sel in response.xpath("//table/tr[2]"):
			print sel.xpath("td/text()").extract()
		accumtulatedP = response.xpath("//table/tr[2]/td/*/text()").extract()
		print accumtulatedP
		item = TaipeiWeatherItem()
		print item