# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from taobao.db.dbhelper import DBHelper


# class MysqlPipeline(object):
#     # 连接数据库
#     def __init__(self):
#         self.db = DBHelper()
#
#     def process_item(self, item, spider):
#         # 插入数据库
#         self.db.insert(item)
#         return item


class TaobaoPipeline(object):

    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        if spider.name == 'get_ip':
            # 插入数据库
            self.db.insert(item)
        else:
            # 获取数据库中ip
            self.db.get_random_ip()
            pass
        return item
