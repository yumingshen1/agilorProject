import yaml
import os
import json
from utils.handle_path import *

def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8')as fo:
        # con = yaml.load(fo,Loader=yaml.FullLoader)
        con = yaml.safe_load(fo.read()) #安全加载
        return con


def get_yaml_data2(yaml_file):
    with open(yaml_file,encoding='utf-8')as f:
        con = yaml.load(f,Loader=yaml.FullLoader)
        print(con)
        print(type(con))
        con = json.dumps(con)
        print(type(con))
        return con


if __name__ == '__main__':
    yamlfile = os.path.join(config_path,'queryData.yml')
    res = get_yaml_data2(yamlfile)
    print(res)
    print(type(res))