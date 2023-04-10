import requests


class GoogleMapAPIPostGet:
    """Создание новых записей в Google Map и проверка, что записи созданы"""
    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'

    def test_creat_new_location(self):
        """Отправляем 5 API запросов и записываем из ответов 5 'place_id' в файлик"""
        post_resource = '/maps/api/place/add/json/'
        post_url = self.base_url + post_resource + self.key
        place_id_file = open("place_id/place_id.txt", 'a')
        for i in range(1, 6):
            # body запроса находится в цикле for, меня в нем "lat" и "name",  что бы создавать немного разные объекты
            lat = '-38.38349' + str(i)
            name = 'Frontline house' + str(i)
            post_body_new_location = {
                "location": {
                    "lat": lat,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": name,
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }
            post_result = requests.post(post_url, json=post_body_new_location)
            self.assert_results('Post', post_result, post_url)
            js_post_result = post_result.json()
            place_id = js_post_result.get("place_id")
            place_id_file.write(f'{place_id}\n')
        place_id_file.close()

    def check_new_location(self):
        """Читаем файлик с 'place_id' и по каждому значению 'place_id' (по каждой строчке) отправлем get запрос"""
        get_resource = '/maps/api/place/get/json'
        place_id_file = open("place_id/place_id.txt", "r")
        while True:
            line = place_id_file.readline()
            if not line:
                break
            get_place_id = f'&place_id={line.strip()}'
            get_url = self.base_url + get_resource + self.key + get_place_id
            get_result = requests.get(get_url)
            self.assert_results('Get', get_result, get_url)
        place_id_file.close()

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


test = GoogleMapAPIPostGet()
test.test_creat_new_location()
test.check_new_location()
