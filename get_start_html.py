import requests

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'accept': '*/*'
    }


def get_html() -> None:
    url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
    req = requests.get(url, headers=headers).text
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(req)
