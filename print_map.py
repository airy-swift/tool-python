import json

if __name__ == '__main__':
    dic_str = input()
    dic = json.load(dic_str)
    for key, value in dic.items():
        print('{0}: {1}'.format(key, value))
