import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__),"config.ini"))


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
