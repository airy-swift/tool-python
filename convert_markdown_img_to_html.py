import re
import pyperclip


def convert_markdown_img_to_html(text):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2" width="350">', text)


if __name__ == '__main__':
    text = pyperclip.paste()
    converted_text = convert_markdown_img_to_html(text)
    print(converted_text)
    pyperclip.copy(converted_text)
