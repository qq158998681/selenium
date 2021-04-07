import sys

from selenium import webdriver
import conf

class Base():
    driver = None

    def __init__(self):
        # 读取浏览器信息，并选择对应的浏览器添加到driver中
        a = conf.message_ini()
        bro, url = a
        if bro == "chrome":
            self.driver = webdriver.Chrome()
        elif bro == "firefix":
            self.driver = webdriver.Firefox()
        elif bro == "ie":
            self.driver = webdriver.Ie()
        else:
            print("您输入的浏览器信息有误")
            sys.exit(0)

        # 读取地址信息
        try:
            self.driver.get(url)
        except :
            print("您的driver驱动与浏览器不匹配")













if __name__ == '__main__':
    a = Base()



