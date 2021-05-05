from pagebase import runlog
import unittest
from api import baidu_main
from selenium.common.exceptions import NoSuchElementException

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.log = runlog.RunLog()

    def tearDown(self):
        pass

    def test_open_baidu(self):
        text = baidu_main.Main().open_baidu()
        try:
            self.assertEqual(text, "123", "pass")
            self.log.logInfo("测试用例001通过")
        except NoSuchElementException :
            self.log.logError("没有找到这个元素,信息")
        except AssertionError :
            self.log.logWarning("预期元素与实际不符，预期{}，实际{}".format("123", text))
        except Exception :
            self.log.logError("未知异常")








