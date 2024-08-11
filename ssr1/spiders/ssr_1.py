import scrapy
from ssr1.items import Ssr1Item
from scrapy import cmdline

class Ssr1Spider(scrapy.Spider):
    name = "ssr_1"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]

    def parse(self, response):
        items = Ssr1Item()
        for i in range(1, 11):
            items["title"] = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[2]/a/h2/text()').get()
            category = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[2]/div[1]/button//span/text()').getall()
            items["category"] = "".join(category)
            items["area"] = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[2]/div[2]/span[1]/text()').get()
            items["score"] = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[3]/p[1]/text()').get()
            items["time"] = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[2]/div[2]/span[3]/text()').get()
            items["publish_time"] = response.xpath('//*[@id="index"]/div[1]/div[1]/div['+str(i)+']/div/div/div[2]/div[3]/span/text()').get()
            print(items)
            yield items
        if(response.xpath('//*[@id="index"]/div[2]/div/div/div/a/@href').get() is not None):
            next_page = "https://ssr1.scrape.center" + response.xpath('//*[@id="index"]/div[2]/div/div/div/a[last()]/@href').get()
            yield scrapy.Request(url=next_page, callback=self.parse)

if __name__ == "__main__":
    cmdline.execute("scrapy crawl ssr_1 --nolog".split())