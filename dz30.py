import json

# данные как на скриншоте
contacts = {
    "1441751072": {
        "name": "ebegbga",
        "tel": "7979251508"
    },
    "6384137383": {
        "name": "daeefed",
        "tel": "6253294228"
    },
    "8186377272": {
        "name": "bdbgeab",
        "tel": "9543402193"
    },
    "7194236131": {
        "name": "gafdbee",
        "tel": "6265065413"
    },
    "3313812937": {
        "name": "gbfddgg",
        "tel": "5668240979"
    }
}

# запись в файл
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=4, ensure_ascii=False)

# чтение из файла
with open("contacts.json", "r", encoding="utf-8") as f:
    contacts = json.load(f)

# вывод всех контактов
for user_id, info in contacts.items():
    print(f"ID: {user_id}, Имя: {info['name']}, Телефон: {info['tel']}")