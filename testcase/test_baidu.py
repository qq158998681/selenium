from pagebase import runlog
import unittest
from api import baidu_main


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.log = runlog.RunLog()

    def tearDown(self):
        a = baidu_main.Main().quit()

    def test_open_baidu2(self):
        text = baidu_main.Main().open_baidu2()
        self.assertEqual(text, "456", "pass")
        self.log.logInfo("测试用例001通过")

    def test_open_baidu(self):
        text = baidu_main.Main().open_baidu3()
        self.assertEqual(text, "123", "pass")
        self.log.logInfo("测试用例001通过")



if __name__ == '__main__':
    unittest.main()



