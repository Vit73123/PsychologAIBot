import re


def main() -> str:
    text = "sdf2, 324234_sdf"
    pattern = re.compile("[\w|^_]+$")
    # if pattern.search(text) or text == '':
    #     print

if __name__ == '__main__':
    main()
