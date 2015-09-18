# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Weixin01Spider(CrawlSpider):
    name = "weixin01"
    allowed_domains = []
    start_urls = (
        'http://mp.weixin.qq.com/s?__biz=MjM5MzQyOTE0MA==&mid=211598568&idx=5&sn=43691fd3d68a8773eb7c46a2f0520b37&3rd=MzA3MDU4NTYzMw==&scene=6#rd',
    )
    # rules = (
    #     # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
    #     Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
    #
    #     # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
    #     Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    # )

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        print response.xpath('//h2[@id="activity-name"]/text()').extract()[0]
        print response.xpath('//div[@id="js_content"]/p/text()').extract()[0]
        print response.xpath('//div[@class="rich_media_meta_list"]/a/text()').extract()[0]
        print response.xpath('//div[@class="rich_media_meta_list"]/em/text()').extract()[0]
