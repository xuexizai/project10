import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from py.xml import html

from test_02.common.readconfigini import url
driver=None

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # 源码是def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport:
    # return TestReport.from_item_and_call(item, call)
    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome=yield
    '''https://onedrive.live.com/view.aspx?resid=1A3107915121FB1A%21105&id=documents&wd=target%28python.one%7CACCEB5FD-E4F2-4F4E-966C-C707CD434F9D%2FSelenium%7C8F3B3697-D971-4B3B-8002-DAD79A17C4A5%2F%29
onenote:https://d.docs.live.net/1a3107915121fb1a/文档/锦辉%20的笔记本/python.one#Selenium&section-id={ACCEB5FD-E4F2-4F4E-966C-C707CD434F9D}&page-id={8F3B3697-D971-4B3B-8002-DAD79A17C4A5}&object-id={3BCC4BB6-FFA5-0127-1377-6F122ABA2075}&D6'''
    # yield是得到hookimpl这个钩子函数的结果
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    #doc这玩意儿用来看注释。
    extra = getattr(report, 'extra', [])
    #获取report extra属性值，没有就自动创建
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        #这里xfail代表预期失败，当用pytest.mark.xfail标记后，就会有xfail属性
        if (report.skipped and xfail) or (report.failed and not xfail):
            #除了预期失败并跳过的，和不是预期失败的失败。都会导致：
            file_name = report.nodeid.replace("::", "_") + ".png"
            #nodeid是由文件名加函数名组成，这里replace把中间的：：换了
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                '''https://onedrive.live.com/view.aspx?resid=1A3107915121FB1A%21105&id=documents&wd=target%28python.one%7CACCEB5FD-E4F2-4F4E-966C-C707CD434F9D%2FSelenium%7C8F3B3697-D971-4B3B-8002-DAD79A17C4A5%2F%29
onenote:https://d.docs.live.net/1a3107915121fb1a/文档/锦辉%20的笔记本/python.one#Selenium&section-id={ACCEB5FD-E4F2-4F4E-966C-C707CD434F9D}&page-id={8F3B3697-D971-4B3B-8002-DAD79A17C4A5}&object-id={3BCC4BB6-FFA5-0127-1377-6F122ABA2075}&C6'''
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))

def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return driver.get_screenshot_as_base64()
if __name__ == '__main__':
    pytest.main()