# -*- coding: utf-8 -*-
import scrapy
from taobao.items import IpItem
import datetime


class GetipSpider(scrapy.Spider):
    name = 'get_ip'
    allowed_domains = ['www.xicidaili.com/wt/']

    urls = ['https://www.xicidaili.com/wt/']
    offset = 1
    start_urls = []
    start_urls.append(urls[0]+str(offset))
    ip_pool = set()

    def parse(self, response):

        ip_item = IpItem()

        # 获取所有行的rt值
        if len(self.ip_pool) == 0:
            tr_node_lists = response.xpath("//tr")
            for tr_one in tr_node_lists:
                try:
                    tr_ip = tr_one.xpath("./td/text()").extract()[0]
                    if len(tr_ip) < 6:
                        continue
                    else:
                        tr_port = tr_one.xpath("./td/text()").extract()[1]
                        tr_ip_type = tr_one.xpath("./td/text()").extract()[5]
                        # tmp_date = str(20)+tr_ip_date[0:8]
                        # ip_date = datetime.datetime.strptime(tmp_date, '%Y-%m-%d')
                        # print('打印tr_ip地址：', tr_ip, tr_ip_date, ip_date)
                        self.ip_pool.add(tr_ip)
                        ip_item['ip_type'] = tr_ip_type
                        ip_item['ip'] = tr_ip
                        ip_item['port'] = tr_port
                        # ip_item['ip_date'] = ip_date
                        yield ip_item
                except:
                    continue

        # print('IP池：', self.ip_pool)
        pass
