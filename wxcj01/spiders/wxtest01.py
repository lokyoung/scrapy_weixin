# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class Wxtest01Spider(scrapy.Spider):
    page=[]
    for i in range(1,11):
        #newspage = 'http://weixin.sogou.com/weixin?query=%E6%96%B0%E9%97%BB&fr=sgsearch&sut=857&lkt=0%2C0%2C0&type=1&sst0=1438930680426&page='+str(i)+'&ie=utf8&w=01019900&dr=1'
        newspage = 'http://weixin.sogou.com/weixin?query=体育&fr=sgsearch&sut=2402&lkt=0%2C0%2C0&type=1&sst0=1439255616169&page='+str(i)+'&ie=utf8&w=01019900&dr=1'
        page.append(newspage)
    name = "wxtest01"
    allowed_domains = []
    start_urls = page
    download_delay = 1

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        url = response.xpath('//div[@class="wx-rb bg-blue wx-rb_v1 _item"]/@href').extract()
        f = open('ylurl.text','a')
        for each in url:
            f.writelines('http://weixin.sogou.com'+each+'\n')
        f.close()

    def parse_next(self, response):
        self.log('A response from %s just arrived!' % response.url)
