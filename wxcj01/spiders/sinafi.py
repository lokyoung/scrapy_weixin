# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor



class SinafiSpider(CrawlSpider):
    page = []
    for i in range(10,301):
        newpage = 'http://roll.finance.sina.com.cn/finance/gncj/hgjj/index_' + str(i)+'.shtml'
        page.append(newpage)
    name = "sinafi"
    allowed_domains = []
    start_urls = page

    def parse(self, response):
        url = response.xpath('//ul[@class="list_009"]/li/a/@href').extract()
        f = open('url01.text','a')
        for each in url:
            f.writelines(each+'\n')
            print each
        f.close()
