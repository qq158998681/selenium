from pagebase import selenium_public
from pagebase import runlog
from selenium.common.exceptions import NoSuchElementException


class Main(selenium_public.Base):
    url = "http://www.baidu.com"

    def open_baidu3(self):
        try:
            self.id("kw").send_keys("123")
            self.id("su").click()
            a = self.css(".c-abstract > em").text
            return a
        except NoSuchElementException:
            self.log.logError("没有定位到这个元素")
            return False
        except Exception:
            self.log.logError("未知异常")
            return False

    def open_baidu2(self):
        try:
            self.id("k").send_keys("123")
            self.id("su").click()
            a = self.css(".c-abstract > em").text
            return a
        except NoSuchElementException:
            self.log.logError("没有定位到这个元素")
            return False
        except Exception:
            self.log.logError("未知异常")
            return False



if __name__ == '__main__':
    a = Main()
    print(a.open_baidu())