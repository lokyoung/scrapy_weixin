# -*- coding: utf-8 -*-
import scrapy
from wxcj01.items import SinafiItem
from wxcj01.spiders.sinafi import SinafiSpider

class SinafaSpider(scrapy.Spider):
    f = open('url.text')
    items=[]
    while 1:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        items.append(line)
    f.close()
    name = "sinafa"
    allowed_domains = []
    start_urls = items

    def parse(self, response):
        # self.log('Hi, this is an item page! %s' % response.url)
        # 标题
        # print response.xpath('//title/text()').extract()[0]
        # 时间
        # time = response.xpath('//span[@class="time-source"]/text()').extract()[0].strip('\n')
        # 内容
        # print response.xpath('//div[@id="artibody"]/p/text()').extract()[0]
        # 信息来源
        # print response.xpath('//span[@class="time-source"]/span/a/text()').extract()[0]
        # 描述
        # print response.xpath('//meta[@name="description"]/@content').extract()[0]
        # 关键词
        # print response.xpath('//meta[@name="keywords"]/@content').extract()[0]

        item = SinafiItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        item['date'] = response.xpath('//span[@class="time-source"]/text()').extract()[0].strip('\n')
        item['source'] = response.xpath('//span[@class="time-source"]/span/a/text()').extract()[0]
        item['des'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
        item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]

        content_field = response.xpath('//div[@id="artibody"]/p/text()').extract()
        mystr = ''
        for each in content_field:
            mystr = mystr + each

        item['content'] = mystr
        yield item
