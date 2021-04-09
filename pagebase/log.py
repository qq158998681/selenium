import logging
import conf


class RunLog:

    def __init__(self):
        logging.basicConfig(
            filename="chrome.log",
            filemode="a",
            format="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(message)s",
            level=logging.INFO
        )

