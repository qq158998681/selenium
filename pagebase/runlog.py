import logging
import conf
import sys
import traceback

# 日志模块


class RunLog():

    def __init__(self):
        a = conf.MessageIni()
        b = a.log()
        c = a.browser()
        if b[1] == "0":
            logging.basicConfig(
                filename=b[0] + "{}.txt".format(c[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.DEBUG

            )
            logging.info("日志初始化成功,当前模式，debug")
        elif b[1] == "1":
            logging.basicConfig(
                filename=b[0] + "{}.txt".format(c[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.ERROR
            )
            logging.info("日志初始化成功,当前模式，info")
        else:
            logging.basicConfig(
                filename=b[0] + "{}.txt".format(c[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.DEBUG
            )
            print("您在配置文件中输入的log信息有误，请重新输入")
            logging.critical("您在配置文件中输入的log信息有误，请重新输入")
            sys.exit(0)

    def logDebug(self, message=None):
        all_message = message + traceback.format_exc()
        return logging.debug(all_message)

    def logInfo(self, message=None):
        all_message = message + traceback.format_exc()
        return logging.info(all_message)

    def logWarning(self, message=None):
        all_message = message + traceback.format_exc()
        return logging.warning(all_message)

    def logError(self, message=None):
        all_message = message + traceback.format_exc()
        return logging.error(all_message + traceback.format_exc())

    def logCritical(self,message=None):
        all_message = message + traceback.format_exc()
        return logging.critical(all_message + traceback.format_exc())


if __name__ == '__main__':
    a = RunLog()
