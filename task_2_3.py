#Основные типы данных:
type_bool = True # Логические (булевые) данные. Могут содержать только True или False (1 или 0)
type_int = 10 # Целые числа. Размер ограничен, только размером оперативной памяти
type_float = 1.10006575675 # Числа с плавающей запятой (дробные числа)
type_str = 'Строка' # Данные в виде строки.
# Значение переменной должно быть заключено в кавычки, одинраные, двойные или тройные.
type_list = ['H', 'E', 'L', 'L', 'O!', 1]  # Список, нумерованные набор объектов.
# Каждый элемент содержит только ссылку на объект. Изменяемый тип данных.
type_typle = ('H', 'E', 'L', 'L', 'O!', 1) # Кортеж. Неизменяемый Тип последовательностей. Может содержать любые типы данных.
type_dict = {'name': 'Иван', 'surname': 'Иванов', 'tel': 79151234567} # Словарь. Набор объктов доступ к которым осуществялется по ключу (key:value). Изменяеный тип данных.

# Данные на разные типы необходимо разделять, для экономии памяти, быстроты действия программы и Разные типы обладают разными свойствами, функциями (методами)



print(type(type_dict))
print(type_dict['tel'])
