# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem


class SbggSpider(scrapy.Spider):
    name = 'watch'
    # 测试
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']
    # allowed_domains = ['sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html']
    # start_urls = ['http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html/']
    allowed_domains = ['s.taobao.com', 'taobao.com', 'login.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E6%89%8B%E8%A1%A8&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&style=list']


    # 重写start_requests方法
    def start_requests(self):
        cookies = {
            ''''''
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        item = TaobaoItem()

        # title_node = response.xpath("//div/text()").extract()

        # print('打印title信息。', title_node)

        file_name = 'data.html'
        with open(file_name, 'wb') as f:
            f.write(response.body)

        # yield item









































