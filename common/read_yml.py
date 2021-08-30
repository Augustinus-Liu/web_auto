import yaml
import os

def readyml(filePath):
    """读取yaml文件"""
    f = open(filePath,"r",encoding="utf-8")
    y = f.read()
    datas = yaml.load(y)

    return datas


if __name__ == '__main__':

    import yaml
    #读取当前脚本的路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path =os.path.join(os.path.dirname(cur_path),"case","data_demo.yml")
    print(yaml_path)
    a = readyml(yaml_path)
    print(a["test_add_project"])