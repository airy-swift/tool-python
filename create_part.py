import os
import re
import sys


def create_file(file_path):
    widget_path_index = file_path.rfind('/')
    widget_path = file_path[:widget_path_index]
    page_dir_index = file_path[:widget_path_index].rfind('/')
    page_path = file_path[:page_dir_index]

    page_file_name = get_page_name(page_path)

    with open(file_path, 'w') as f:
        f.write("part of '../{}';\n".format(page_file_name))


def get_page_name(parent_oath):
    page_path = ""
    for dirpath, dirnames, filenames in os.walk(parent_oath):
        # ファイル名が一致するかを検索
        for filename in filenames:
            if re.search("(\w+)_page.dart", filename):
                # ファイルパスを取得
                page_path = filename
    return page_path


if __name__ == '__main__':
    create_file(sys.argv[1])
