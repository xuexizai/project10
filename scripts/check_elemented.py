import os
import yaml
from test_02.config.conf import cm
from test_02.utils.times import func_times
@func_times
def check_elemented():
    path=os.listdir(cm.ELEMENT_PATH)
    for file in path:
        files=os.path.join(cm.ELEMENT_PATH, file)
        with open(files, encoding='utf-8')as f:
            data = yaml.safe_load(f)
        if data:
            for k in data.value:
                try:
                    option, value = k.split('==')
                except:
                    raise Exception("元素表达式中没有`==`")
                try:
                    cm.LOCATE_MODE[option]
                except:
                    raise Exception(f'{files}中没有{option}类型')
    return "elements is ok"
if __name__ == '__main__':
    check_elemented()
