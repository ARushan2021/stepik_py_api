import requests


url = 'https://api.chucknorris.io/jokes/random'
result = requests.get(url)
assert result.status_code == 200
result.encoding = 'utf-8'
js = result.json()
jack = js.get('value')
#response = result.text
#print(jack)
#print(type(jack))


result1 = requests.get('https://api.chucknorris.io/jokes/categories')
#print(result1.text)

json_put = {
    "place_id": 345345345
}

print(type(json_put))