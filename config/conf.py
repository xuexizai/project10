#用来配置根，日志，元素，报告，配置，邮箱路径和方法属性的
import os
from test_02.utils.times import st_time,nowtime
from selenium.webdriver.common.by import By
class ConfigManager():
    def __init__(self):
        self.LOCATE_MODE = {
#写入定位方式和调用de方法
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'id': By.ID,
            'class': By.CLASS_NAME
        }
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ELEMENT_PATH=os.path.join(self.BASE_DIR, 'page_element')
        self.REPORRT_FILE=os.path.join(self.BASE_DIR, 'report')
        self.EMAIL_INFO = {
            'username': '3151549710@qq.com',
            'password': 'zpopptcvprpadhab',
            'smtp_host': 'smtp.qq.com',
            'smtp_port': 465
        }
        self.ADDRESSEE = [
            '3151549710@qq.com',
        ]

    @property
    def log_file(self):

        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, f'{st_time(nowtime())}.log')
    #这是确定log_file位置
    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file
    #告诉你config.ini的位置
cm = ConfigManager()
if __name__ == '__main__':
    print(cm.log_file)
    print('#用来配置根，日志，元素，报告,配置，邮箱路径和方法属性的')