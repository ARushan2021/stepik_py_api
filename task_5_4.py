import requests


def all_categories_chuck_norris():
    """Извлекаем список доступных категорий шуток про Чака Норриса и записываем их в переммую"""
    all_categories_url = 'https://api.chucknorris.io/jokes/categories'
    all_categories_result = requests.get(all_categories_url)
    assert all_categories_result.status_code == 200, 'Где-то закралась ошибка!'
    all_categories_result.encoding = 'utf-8'
    categories = all_categories_result.json()
    return categories


def chuck_norris_joke_all_categories(categories):
    """Создание случайно шутки из каждой категории про Чака Норриса"""
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


chuck_norris_joke_all_categories(all_categories_chuck_norris())



# Решение #931968682
# Здравствуйте. Рушан, категории нужно брать из ответа первого запроса (он указан в задании),
# а не писать список, так как если категории изменятся, то мы не будем иметь актуальной информации.
# Решение можно дослать на aleksandr_stepik@mail.ru
