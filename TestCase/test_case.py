import pytest

from test_02.utils.logger import log
#fadsfa
from test_02.scripts.check_elemented import check_elemented
from test_02.config.conf import cm
from test_02.utils.times import *
from test_02.utils.web_method import *
try:
    check_elemented()
except:
    raise Exception('elements has problem')

class TestCase:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        drivers.get(url.get('HOST', 'HOST'))
        drivers.implicitly_wait(10)
    def test_001(self, drivers):
        act=Kb_Ms(0, drivers)
        result=act.locate_element()
        assert result
if __name__ == '__main__':
    pytest.main(['test_02/TestCase/test_case.py'])
