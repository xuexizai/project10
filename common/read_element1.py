# -*- coding:utf-8 -*-
import os
import yaml
from test_02.config.conf import cm

class Read_Element():
    def __init__(self,num):
        self.file_name = os.listdir(cm.ELEMENT_PATH)[num]
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError(f"{self.element_path} 文件不存在！" )
        with open(self.element_path, encoding='utf-8')as f:
            self.data = yaml.safe_load_all(f)
    # 使用Read_Element[name]命令后python会自动调用__getitem__函数
    def __getitem__(self, item):
        data=self.data.get(item)
        if data:
            [option, value] = data.split('==')
            return option, value
        raise Exception (f'{self.file_name} doesnt exist this')

element_info = Read_Element(0)
elemented=element_info['搜索框']

if __name__ == '__main__':
    search = Read_Element(0)
    print(search['搜索框'])


