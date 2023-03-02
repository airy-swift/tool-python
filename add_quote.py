import sys
import pyperclip


def copy_to_clipboard(text):
    pyperclip.copy(text)


def add_quotes(text):
    key_value_list = [key_value.strip() for key_value in text.split(",")]
    new_list = []
    for key_value in key_value_list:
        key, value = key_value.split(":", maxsplit=1)
        new_list.append('\t"' + key.strip() + '"' + ":" + '"' + value.strip() + '"')
    return ",\n".join(new_list)


if __name__ == "__main__":
    args = sys.argv
    file_path = args[1]
    with open(file_path) as f:
        text = f.read()
    result = add_quotes(text)
    print(result)
    copy_to_clipboard(result)
    print("... and copied!!")