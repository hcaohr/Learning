import yaml


def get_yaml_data(yaml_file):
    # 打开yaml文件
    print("***获取yaml文件数据***")
    # file = open(yaml_file, 'r', encoding="utf-8")
    # file_data = file.read()
    # file.close()
    with open(yaml_file, mode='r', encoding='utf-8') as file:
        file_data = file.read()

    print(file_data)
    print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader=yaml.safe_load)
    print(data)
    print("类型：", type(data))
    return data


get_yaml_data('data.yml')
