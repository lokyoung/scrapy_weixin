# -*- coding: utf-8 -*-
import scrapy
from wxcj01.items import SinafiItem

class Sinafi01Spider(scrapy.Spider):
    f = open('url01.text')
    items=[]
    while 1:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        items.append(line)
    f.close()
    name = "sinafi01"
    allowed_domains = []
    start_urls = items

    def parse(self, response):
        # print response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        # print response.xpath('//span[@id="pub_date"]/text()').extract()[0]
        # print response.xpath('//span[@id="media_name"]/a/text()').extract()[0]
        # print response.xpath('//meta[@name="description"]/@content').extract()[0]
        # print response.xpath('//meta[@name="keywords"]/@content').extract()[0]
        # print response.xpath('//div[@id="artibody"]/p/text()').extract()[0]
        item = SinafiItem()

        item['title'] = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        item['date'] = response.xpath('//span[@id="pub_date"]/text()').extract()[0]
        item['source'] = response.xpath('//span[@id="media_name"]/a/text()').extract()[0]
        item['des'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
        item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]

        content_field = response.xpath('//div[@id="artibody"]/p/text()').extract()
        mystr = ''
        for each in content_field:
            mystr = mystr + each

        item['content'] = mystr
        yield item
