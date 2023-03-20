from parsing import parsing
from create_json_and_csv import create_files
from get_start_html import get_html


def main():
    get_html()
    data = parsing()
    create_files(data)


if __name__ == '__main__':
    main()
