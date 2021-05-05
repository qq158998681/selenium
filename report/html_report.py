import unittest
from BeautifulReport import BeautifulReport
import time


class html_report():

    def make_report(self):
        test_suite = unittest.defaultTestLoader.discover(r'./testcase', pattern='test*.py')
        result = BeautifulReport(test_suite)
        html_name = time.strftime("%Y-%m-%d", time.localtime()) + "测试报告"
        return result.report(filename=html_name, description='测试报告', report_dir='./', theme='theme_default')


if __name__ == '__main__':
    a = html_report()
    a.make_report()




