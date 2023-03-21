import csv
import json


def create_files(data: list[list[str, str, str, str, str], ...]) -> None:
    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['Section', 'Products', 'Сalories', 'Proteins', 'Fats', 'Carbohydrates'])
        writer.writerows(data)

    json_data = [{'Section': i[0], 'Products': i[1], 'Сalories': i[2], 'Proteins': i[3], 'Fats': i[4], 'Carbohydrates': i[5]}
                 for
                 i in data]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
