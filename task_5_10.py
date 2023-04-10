import requests


class GoogleMapAPIDeleteGet:
    """Удаление записей в Google Map по place_id из файлика и проверка оставшихся place_id из файлика get запросом"""

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'

    def delete_new_location(self):
        """Удаляем 2-ю и 3-ю запись по place_id из файлика"""
        delete_resource = '/maps/api/place/delete/json'
        delete_url = self.base_url + delete_resource + self.key
        place_id_file = open("place_id/place_id.txt", 'r')
        place_all_id = place_id_file.readlines()
        for i in range(1, 4, 2):
            place_id = place_all_id[i]
            delete_body = {
                "place_id": place_id[:-1]
            }
            delete_result = requests.delete(delete_url, json=delete_body)
            self.assert_results('Delete', delete_result, delete_url)
        place_id_file.close()

    def check_location_from_file(self):
        """Читаем файлик с 'place_id' и по каждому значению 'place_id' (по каждой строчке) отправлем get запрос,
        если запись найдена, то сохраняем 'place_id' в новый файл"""
        get_resource = '/maps/api/place/get/json'
        place_id_file = open("place_id/place_id.txt", "r")
        place_id_new_file = open("place_id/new_place_id.txt", "w")
        while True:
            line = place_id_file.readline()
            if not line:
                break
            get_place_id = f'&place_id={line.strip()}'
            get_url = self.base_url + get_resource + self.key + get_place_id
            get_result = requests.get(get_url)
            print(f"'Get' запрос со cтатус код: {get_result.status_code}")
            if get_result.status_code == 200:
                place_id_new_file.write(f'{line.strip()}\n')
                print(f'status_id : "{line.strip()}" записан в файл new_place_id.txt')
        place_id_file.close()
        place_id_new_file.close()

    def assert_results(self, request_type, result, url):
        """Проверяем код статуса запроса - 200 и выводим в консоль тип запроса, статус(если Post), код статуса, url"""
        assert result.status_code == 200, f"Статус код - {result.status_code},  где-то ошибка!"
        js_result = result.json()
        status = js_result.get("status")
        if request_type == "Post":
            print(f"'{request_type}' запрос успешен! Статус: {status}, код: {result.status_code}")
        else:
            print(f"'{request_type}' запрос успешен! Статус код: {result.status_code}")
        print(url)


test = GoogleMapAPIDeleteGet()
test.delete_new_location()
test.check_location_from_file()
