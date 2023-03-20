import requests
from bs4 import BeautifulSoup
from get_start_html import headers


def parsing() -> list[list[str, str, str, str, str], ...]:
    data = []

    with open('index.html', 'r', encoding='utf-8-sig') as f:
        file = f.read()

    soup = BeautifulSoup(file, 'lxml')

    links_to_eat = {i.find('span').text: f'https://health-diet.ru{i.get("href")}' for i in
                    soup.find_all('a', class_='mzr-left-menu-item uk-link-reset')}

    for url in links_to_eat:
        req = requests.get(links_to_eat[url], headers=headers).text
        soup = BeautifulSoup(req, 'lxml')
        eat_info_html = [[url] + [j.text.strip() for j in i.find_all('td')] for i in soup.find('tbody').find_all('tr')]
        data.extend(eat_info_html)

    return data
