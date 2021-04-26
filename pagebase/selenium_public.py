import sys
from selenium import webdriver
import runlog
import conf


# 该类为定位元素的公共方法


class Base():
    driver = None
    url = ""

    def __init__(self):

        self.log = runlog.RunLog()
        # 环境准备，将ini文件中的信息自动读取，并且处理
        # 读取浏览器信息，并选择对应的浏览器添加到driver中
        a = conf.MessageIni()
        bro = a.browser()[0]
        url = a.test_address()
        driver_path = a.driver_path()
        try:
            if bro == "chrome":
                self.driver = webdriver.Chrome(driver_path)
            elif bro == "firefix":
                self.driver = webdriver.Firefox(driver_path)
            elif bro == "ie":
                self.driver = webdriver.Ie(driver_path)
            else:
                print("您输入的浏览器信息有误,请检查并修改")
                self.log.logCritical("您输入的浏览器信息有误")
                sys.exit(0)
        except Exception:
            print("未知错误")
            self.log.logCritical("未知错误")
            sys.exit(0)


        # 读取地址信息
        try:
            self.driver.get(url)
        except :
            print("您输入的测试地址无法识别，请检查并修改")
            self.log.logCritical("您输入的测试地址无法识别")
            sys.exit(0)

    def id(self, ele):
        return self.driver.find_element_by_id(ele)

    def class_name(self, ele):
        return self.driver.find_element_by_class_name(ele)

    def text(self, ele):
        return self.driver.find_element_by_link_text(ele)

    def part_text(self, ele):
        return self.driver.find_element_by_partial_link_text(ele)

    def css(self, ele):
        return self.driver.find_element_by_css_selector(ele)

    def xpath(self, ele):
        return self.driver.find_element_by_xpath(ele)

    def name(self, ele):
        return self.driver.find_element_by_name(ele)

    def tag_name(self, ele):
        return self.driver.find_element_by_tag_name(ele)

    def ids(self, ele):
        return self.driver.find_elements_by_id(ele)

    def class_names(self, ele):
        return self.driver.find_elements_by_class_name(ele)

    def textes(self, ele):
        return self.driver.find_elements_by_link_text(ele)

    def part_textes(self, ele):
        return self.driver.find_elements_by_partial_link_text(ele)

    def csses(self, ele):
        return self.driver.find_elements_by_css_selector(ele)

    def xpaths(self, ele):
        return self.driver.find_elements_by_xpath(ele)

    def names(self, ele):
        return self.driver.find_elements_by_name(ele)

    def tag_names(self, ele):
        return self.driver.find_elements_by_tag_name(ele)

    def quit(self):
        return self.driver.quit()


if __name__ == '__main__':
    a = Base()




