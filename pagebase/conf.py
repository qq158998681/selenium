import configparser


# 获取配置文件数据，并加入到driver

def message_ini():
    # 读取ini文件
    config = configparser.ConfigParser()
    a = config.read("../config/config.ini", encoding="utf-8")
    # 获取数据
    i = config.get("browser", "bro")
    j = config.get("address", "url")

    return i, j


if __name__ == '__main__':
    print(message_ini())

