import os
import yaml
from test_02.config.conf import cm

class Read_Element():
    def __init__(self, name):
        self.file_name = f'{name}.yaml'
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError(f"{self.element_path} 文件不存在！" )
        f=open(self.element_path, 'r', encoding='utf-8')
        self.data=yaml.safe_load(f)
    # 使用Read_Element[name]命令后python会自动调用__getitem__函数
    def getitem(self):
        elemented = []
        for i in self.data.values():
            try:
                option, value = i.split('==')
                elemented.append((option, value))
            except:
                raise Exception(f'{self.file_name} doesnt exist {i}')
        return elemented


element_info = Read_Element('element')

if __name__ == '__main__':
    search = Read_Element('element')
    print(search.getitem())
    print('nihao')
