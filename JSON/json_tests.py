import json
from pathlib import Path


class Test1:
    def load_json_file(self):
        json_path = Path('Test_Result.json')
        # 读取JSON数据
        with open(json_path, 'rt') as f:
            result = json.load(f)
        print(result)

    def dump_json_file(self):
        json_path = Path('dump_json.json')
        t_dict = {
            'test1': 1,
            'test2': 2,
            'test3': 3
        }
        # 判断文件是否存在，不存在则新建
        if not json_path.is_file():
            json_path.touch()
            a = [t_dict]
        else:
            with open(json_path, 'r') as f:
                result = json.load(f)
            a = result
            a.append(t_dict)
        # 写入JSON文件
        with open(json_path, 'w') as f:
            json.dump(a, f)


if __name__ == "__main__":
    Test1().dump_json_file()
