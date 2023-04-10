import requests


class ChuckNorrisJoke:
    """Шутки от Чака Норриса по определенной категории"""

    def __init__(self):
        pass

    def input_category(self):
        """Ввод категории шутки про Чакка Норриса и проверка, что есть такая категория"""
        input_category = input('Введите категорию шуток про старину Чака: ').lower()
        result = requests.get('https://api.chucknorris.io/jokes/categories')
        status_code = result.status_code
        assert status_code == 200, 'Где-то закралась ошибка!'
        result.encoding = 'utf-8'
        categories_str_new = result.text[1:-1].replace('"', '')
        categories_list = categories_str_new.split(',')
        checking_category = input_category in categories_list
        if checking_category is False:
            print('Такой категории нет в шутках, но Чака Норриса это никогда не останавливало...')
            exit()
        return input_category

    def chuck_norris_joke_all_categories(self):
        """Создание случайно шутки из определенной категории про Чака Норриса"""
        category = self.input_category()
        result = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
        status_code = result.status_code
        assert status_code == 200, 'Где-то закралась ошибка!'
        result.encoding = 'utf-8'
        js = result.json()
        joke = js.get('value')
        print(f'Статус кода - {status_code}\nШутка про Чака Норриса в категории "{category}": {joke} ')


task_5_5 = ChuckNorrisJoke()
task_5_5.chuck_norris_joke_all_categories()
