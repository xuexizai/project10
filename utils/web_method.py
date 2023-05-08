from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from functools import partial
from selenium.webdriver.common.keys import Keys

from test_02.common.readconfigini import url
from test_02.config.conf import cm
from test_02.common.read_element import *
from test_02.utils.logger import log

# @pytest.fixture(scope='session', autouse=True)
# def initialize_web(request):
    #这里的request是fixture的一种，用来传递其他fixture参数，在这里主要是继承
    #fixture的一个开头和结束的功能。
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
url1=url.get('HOST', 'HOST')
driver.get(url1)
driver.maximize_window()
    # def end():
    #     driver.quit()
    # request.addfinalizer(end)
    # return driver

class Locate_Element():
    def __init__(self, ele):
        self.elemented=element_info[ele]
        self.timeout = 10

        self.wait = WebDriverWait(driver, self.timeout)
        #这是一个显示的等待，等待10s时间中等待后面条件发生，如果未发生报出超时问题，
        # 在等待过程中默认每0.5s访问一下看条件是否发生

    @staticmethod
    def locate(func, eles):
        option, value=eles
        return func(getattr(By, option), value)

    #这个函数主要是用来分离定位信息的，将定位信息完整的获取，并返回在下面的函数中
    def locate_element(self):
        print(f"now find {self.elemented}" )
        return Locate_Element.locate(lambda *args: self.wait.until\
        (EC.presence_of_element_located(args)), self.elemented)

    #这个函数是调用上述定位信息函数，来查找元素，其中lambda接受*args任意参数输入，
    #输入的参数变成一个tuple也就是args一起输入到函数中。
    #这里如果想要value这个函数可以直接result, value=return 后面一大串
    #就可以在这个函数中随便用value,最后再return result就行
    def locate_elements(self):
        print("now find all %s" % (self.elemented))
        return Locate_Element.locate(lambda *args: self.wait.until\
        (EC.presence_of_all_elements_located(args)), self.elemented)

    def elements_num(self):
        number = len(self.locate_elements(self.elemented))
        log.info(f"same element: {(self.elemented,number)}")
        return number
class Kb_Ms(Locate_Element):
    def __init__(self):
        super().__init__()
        def action(self, actions, *args):
            actions(self.locate_element(), *args).perform()
        self.left_click = partial(action, actions=ActionChains(driver).click)
        self.right_click = partial(action, actions=ActionChains(driver).context_click)
        self.double_click = partial(action, actions=ActionChains(driver).double_click)
        self.click_hold = partial(action, actions=ActionChains(driver).click_and_hold)
        self.mv_to_ele = partial(action, actions=ActionChains(driver).move_to_element)
        self.send_keys = partial(action, actions=lambda element, keys: \
            ActionChains(driver).send_keys_to_element(element, keys))
        self.submit = partial(action, actions=lambda element: \
            ActionChains(driver).key_down(Keys.ENTER, element))


    def refresh(self):
        """刷新页面F5"""
        driver.refresh()
        driver.implicitly_wait(10)

ele='搜索框'
act=Locate_Element(ele)
act.locate_element()





