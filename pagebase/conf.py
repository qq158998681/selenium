import configparser


# 获取配置文件数据

class MessageIni(object):

    def __init__(self):
        # 读取ini文件
        self.config = configparser.ConfigParser()
        self.config.read("./config/config.ini", encoding="utf-8")

    def browser(self):
        # 读取浏览器相关设置
        browser_type = self.config.get("browser", "browser_type")
        current_browser = self.config.get("browser", "current_browser")
        browser_port = self.config.get("browser", "browser_path")
        browser_path = self.config.get("browser", "browser_port")

        return browser_type, current_browser, browser_port, browser_path

    def test_address(self):
        # 读取测试地址
        url = self.config.get("address", "url")

        return url

    def driver_path(self):
        # 读取driver地址
        driver_path = self.config.get("path", "driver_path")

        return driver_path

    def report_path(self):
        # 读取测试报告地址
        test_report_path = self.config.get("path", "test_report_path")

        return test_report_path

    def log(self):
        # 读取日志级别及日志地址
        log_level = self.config.get("log", "log_level")
        log_path = self.config.get("log", "log_path")

        return log_path, log_level

    def email_message(self):
        # 读取设置的邮箱信息
        email_address = self.config.get("email", "email_addressee")
        email_sender = self.config.get("email", "email_sender")
        email_sender_password = self.config.get("email", "email_sender_password")
        email_host = self.config.get("email", "email_host")
        email_conf = self.config.get("email", "email_conf")

        return email_address, email_sender, email_sender_password, email_host, email_conf

    def test_data_excel(self):
        # 读取测试数据的存放地址及目标sheet
        test_data_path = self.config.get("test_data", "test_file_path")
        test_file_sheet_name = self.config.get("test_data", "test_file_sheet_name")

        return test_data_path, test_file_sheet_name


if __name__ == '__main__':
    a = MessageIni()
    # print(a.log())
    # print(a.browser())
    # print(a.driver_path())
    # print(a.report_path())
    print(a.address())
    print(a.email_address)


