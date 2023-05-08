from test_02.config.conf import cm
import configparser
import sys
HOST='HOST'
class ReadConfig():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(cm.ini_file, encoding='utf-8')
    def __set(self, section, option, value):
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w')as f:
            self.config.write(f)
    def get(self, section, option):
        return self.config.get(section, option)
    #如果有多个url需要访问怎么设置
url = ReadConfig()
if __name__ == '__main__':
    print('用来获取访问地址的')
