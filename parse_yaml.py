import yaml
import sys


def parse_yaml(yaml_path):
    with open(yaml_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    result = {}
    for key, value in data.items():
        result[key] = {}
        for inner_key, inner_value in value.items():
            if inner_key == 'group':
                result[key][inner_key] = {}
                for group_key, group_value in inner_value.items():
                    result[key][inner_key][group_key] = {}
                    for group_key2, group_value2 in group_value.items():
                        result[key][inner_key][group_key][group_key2] = group_value2
            else:
                result[key][inner_key] = inner_value
    return result


def parse():
    yaml_path = sys.argv[1]
    result = parse_yaml(yaml_path)
    return result


if __name__ == "__main__":
    result = parse()
    print(result)
