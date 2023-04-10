st = "ivan"
num = "ivanov"
sum_sum = '{} {}'
print(f'имя и фамилия вместе: {st + num}')


def result_sum(var1, var2):
    res_sum = f'имя и фамилия вместе: {var1 + var2}'
    return print(res_sum)


result_sum(st, num)


fw = open('file/file.txt', 'a')
for i in range(0, 11):
    fw.write(f'{i},')
fw.close()




