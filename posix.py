# import re
# import webbrowser
#
# # 入力を読み込み、1行1要素のlistを作成
# def make_list(file_name):
#     with open(file_name, "r") as f:
#         lst = f.readlines()
#     for i in range(len(lst)):
#         lst[i] = lst[i].strip('\n')
#     return lst
#
#
# # 正規表現を使って、ll=から&までの文字列を抽出
# def get_ll(lst):
#     result = []
#     for l in lst:
#         result.append(re.search('ll=(.*?)&', l).group(1))
#     return result
#
#
# # 各要素の次の要素と/を間に挟んで結合したstrを出力
# def make_str(lst):
#     result = []
#     for i in range(len(lst) - 1):
#         result.append(lst[i] + '/' + lst[i + 1])
#     return result
#
#
# # メイン関数
# def main():
#     file_name = 'position.txt'
#     lst = make_list(file_name)
#     ll_lst = get_ll(lst)
#     result = make_str(ll_lst)
#
#     for i in result:
#         url = "https://www.google.com/maps/dir/" + i + "/data=!3m1!4b1!4m2!4m1!3e3"
#         webbrowser.open_new_tab(url)
#         print(url)
#
#
# if __name__ == '__main__':
#     main()

import webbrowser


def func(list):
    for i in range(len(list) - 1):
        url = "https://www.google.com/maps/dir/" + str(list[i]) + "/" + str(list[i + 1]) + "/data=!3m1!4b1!4m2!4m1!3e3"
        webbrowser.open_new_tab(url)
        print(url)


def read_position():
    position_list = []
    with open('position.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue
            position_list.append(line.strip().split(' ')[0])
    return position_list


read_lines = read_position()
func(read_lines)

########################################

# def input_words():
#     words = []
#     while True:
#         word = input("Please enter a word: ")
#         if word == "END":
#             break
#         words.append(word)
#     return words
#
#
# def output_words():
#     words = input_words()
#     if len(words) > 1:
#         for i in range(len(words) - 1):
#             url = "https://www.google.com/maps/dir/" + words[i] + "/" + words[i + 1]
#             webbrowser.open_new_tab(url)
#             print(url)
#
#     else:
#         print("Please enter more than 2 words")
#
#
# output_words()
