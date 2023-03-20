import csv
import json


def create_files(data: list[list[str, str, str, str, str], ...]) -> None:
    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['Раздел', 'Продукт', 'Калорийность', 'Белки', 'Жиры', 'Углеводы'])
        writer.writerows(data)

    json_data = [{'Раздел': i[0], 'Продукт': i[1], 'Калорийность': i[2], 'Белки': i[3], 'Жиры': i[4], 'Углеводы': i[5]}
                 for
                 i in data]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
