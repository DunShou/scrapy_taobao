import pymysql
from twisted.enterprise import adbapi
# 导入settings配置
from scrapy.utils.project import get_project_settings
import time,requests


class DBHelper():
    """
    读取settings中的配置
    """

    def __init__(self):
        # 获取settings配置，设置需要的信息
        settings = get_project_settings()

        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8', # 编码要加上，防止出现中文乱码
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
#         **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    # 创建数据库
    def insert(self, item):
        sql = "insert into ip_pool(ip_type, ip, port) values(%s, %s, %s)"
        # 调用插入的方法
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        # 调用异常处理方法
        query.addErrback(self._handle_error)

        return item

    # 删除无效ip
    def delete_ip(self, id):
        sql = "delete from ip_pool where id={0}".format(id)
        self.dbpool.runQuery(sql)
        return True

    # 获取随机IP
    def get_random_ip(self):
        self.test_query_ip().addCallback(self.judge_ip)
        """
        random_sql = "SELECT ip_type, ip, port FROM ip_pool ORDER BY RAND() LIMIT 1"

        # 测试查询操作
        # result = self.dbpool.runInteraction(self.rand_sql, random_sql)
        result = self.dbpool.runQuery(random_sql)
        # for result_one in result:
        #     print('测试结果中：', result_one)
        print('测试是否可以查询到：', result[0])
        # 调用异常处理方法
        result.addErrback(self._handle_error)
        return None
        # < Deferred at 0x158b19d2668 >
        # for ip_info in self.dbpool.f"""

    def test_query_ip(self):
        random_sql = "SELECT id, ip_type, ip, port FROM ip_pool ORDER BY RAND() LIMIT 1"
        return self.dbpool.runQuery(random_sql)

    def judge_ip(self, ip_pool):
        if ip_pool:
            # print('判断ip中：', ip_pool)
            http_url = "http://www.baidu.com"
            if ip_pool[0]['ip_type'] is None:
                ip_pool[0]['ip_type'] = 'http'
            # proxy_url = "{0}://{1}:{2}".format(ip_pool[0]['ip_type'], ip_pool[0]['ip'], ip_pool[0]['port'])
            proxy_url = "{0}:{1}".format(ip_pool[0]['ip'], ip_pool[0]['port'])
            # proxy_url = "{0}:{1}".format('99.99.99.99', '9999')
            print('获取的代理url:'+proxy_url)
            try:
                # proxy_dict = {
                #     type: proxy_url,
                # }
                proxy_dict = {
                    ip_pool[0]['ip_type']: proxy_url,
                }
                response = requests.get(http_url, proxies=proxy_dict)
                code = response.status_code
                if code >= 200 and code < 300:
                    print('有效ip地址！')
                    return True
                else:
                    print('失效的ip地址！code值问题。')
                    self.delete_ip(ip_pool[0]['id'])
                    return False
            except:
                self.delete_ip(ip_pool[0]['id'])
                print('失效的ip地址。')
                return False
        else:
            print('没有通过判断，即没有获取到ip！')

    # 写入数据库中
    def _conditional_insert(self, tx, sql, item):
        # item['ip_date'] = time.strftime('%Y-%m-%d %H:%M:%S',
        #                                    time.localtime(time.time()))
        params = (item["ip_type"], item["ip"], item['port'])
        tx.execute(sql, params)

    # 查询
    # def rand_sql(self, tx, random_sql):
    #     tx.execute(random_sql)
    #     result = tx.fetchall()
    #     if result:
    #         print('测试查询中fetchall:', result)
    #         return result[0][0]
    #     else:
    #         print('result没有数据。')
    #         return None

    # 错误处理方法

    def _handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
        print(failue)

    def close_spider(self, spider):
        self.dbpool.close()

































