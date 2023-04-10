import pytest as pytest


#pytest -s -v                - запуск тестов
#pytest -s -v test_mail.py   -  запуск определеннго модуля(файлика)


# module - conftest.py
@pytest.fixtere() # выполняется до теста, в каждой функции где пропишем set_up()
def set_up():
    print('Вход в систему')
    yield         # выполняется после теста
    print('Выход из системы')

@pytest.fixtere(scope="module") # выполняется модуля(файлика), в каждой функции где пропишем some()
              #(scope="cls")
              #(scope="function")
def some():
    print('Вход в систему')
    yield         # выполняется после теста
    print('Выход из системы')


@pytest.mark.run(order=1) # очередность запуска методов
               #(order=2)
def first_function():
    print('Хеллоу ворлд')

