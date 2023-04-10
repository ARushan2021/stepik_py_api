import requests


def chuck_norris_joke_all_categories():
    """Создание случайно шутки из каждой категории про Чака Норриса"""
    categories = ["animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history", "money",
                  "movie", "music", "political", "religion", "science", "sport", "travel"]
    for i in range(0, len(categories)):
        category = categories[i]
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        result = requests.get(url)
        status_code = result.status_code
        assert status_code == 200, 'Где-то закралась ошибка!'
        result.encoding = 'utf-8'
        js = result.json()
        joke = js.get('value')
        print(f'{i + 1}. Статус кода - {status_code}\nШутка про Чака Норриса в категории "{category}": {joke} ')


chuck_norris_joke_all_categories()
