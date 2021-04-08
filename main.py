from pagebase.pagebase import Base


class Index():
    driver = Base()
    def __init__(self):
        pass

    def zhuce(self):
        self.driver.class_name("index_head_info_pCDownloadBtn").click()
        return 





if __name__ == '__main__':
    a = Index()
    a.zhuce()






