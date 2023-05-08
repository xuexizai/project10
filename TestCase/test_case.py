

from test_02.utils.logger import log
from test_02.utils.web_method import *
from test_02.scripts.check_elemented import check_elemented
from test_02.config.conf import cm
from test_02.utils.times import *
try:
    check_elemented()
except:
    raise Exception('elements has problem')



