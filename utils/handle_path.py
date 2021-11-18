import os

# print(__file__)
# print(os.path.dirname(__file__))

## 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)

## 配置路径
config_path = os.path.join(project_path,'configs')
# print(config_path)