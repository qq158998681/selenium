import logging
import conf
import sys


class RunLog():

    def __init__(self):
        a = conf.message_ini()
        if a[3] == "0":
            logging.basicConfig(
                filename="./log/{}.txt".format(a[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.DEBUG

            )
            logging.info("日志初始化成功,当前模式，debug")
        elif a[3] == "1":
            logging.basicConfig(
                filename="./log/{}.txt".format(a[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.ERROR
            )
            logging.info("日志初始化成功")
        else:
            logging.basicConfig(
                filename="./log/{}.txt".format(a[0]),
                filemode="a",
                format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
                level=logging.DEBUG
            )
            logging.critical("您输入的log信息有误，请重新输入")
            sys.exit(0)

    def log_debug(self, message):
        return logging.debug(message)

    def logInfo(self, message):
        return logging.info(message)

    def logWarning(self, message):
        return logging.warning(message)

    def logError(self, message):
        return logging.error(message)

    def logCritical(self,message):
        return logging.critical(message)


if __name__ == '__main__':
    a = RunLog()
