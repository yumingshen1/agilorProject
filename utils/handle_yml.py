import yaml

def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8')as fo:
        # con = yaml.load(fo,Loader=yaml.FullLoader)
        con = yaml.safe_load(fo.read()) #安全加载
        return con

if __name__ == '__main__':
    res = get_yaml_data('../configs/apiConfig.yml')
    header = res['Write']['write']['headers']
    print(res)
    print(header)
    print(type(res))