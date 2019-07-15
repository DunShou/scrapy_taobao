class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "UM_distinctid=1696d53fff232f-08096787c586ac-5b412a18-1fa400-1696d53fff919a; cna=AM7xFMuVn3YCAXkgtalj8Xhq; t=482256acd3ddc13f4f724f829382fc8e; thw=cn; tracknick=%5Cu76FE%5Cu5B881234; _cc_=VT5L2FSpdA%3D%3D; tg=0; enc=YflGyrI57KZDKJrxKy6CS96mNC%2F3pY6OoTDjVBWPvyOnAr8aDuY0XDPqcd7dMwRZgQqf9OT%2BqKrjov74WzjW5Q%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=1366517952401393773; v=0; cookie2=12bedeeebcddd74238e2815b4791105f; _tb_token_=7b3b1b48ee58b; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=DA931CCA86394E658C14A64072876319; l=cBQ3WF0nveG3bfl9BOCNVuIRXSbOSIRASuPRwk_Xi_5ho6L_gl7OkcZYeFp62jWd9HYB41jxjk99-etkNLe06Pt-g3fP.; isg=BDw8Svu2TeZbEHgVvUV7kfjVDdouncs_lPL8aRa9SCcK4dxrPkWw77JRxEk8hBi3"
    trans = transCookie(cookie)
    print(trans.stringToDict())