from pagebase import selenium_public
from pagebase import runlog


class Main(selenium_public.Base):
    url = "http://www.baidu.com"

    def open_baidu(self):
        self.id("kw").send_keys("123")
        self.id("su").click()
        a = self.css(".c-abstract > em").text
        return a

if __name__ == '__main__':
    a = Main()
    print(a.open_baidu())