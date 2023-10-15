# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
import random


def gen_random(num_count, begin, end):
    # Необходимо реализовать генератор
    a = []
    while num_count > 0:
        b = random.randint(begin,end)
        a.append(b)
        num_count -= 1
    return a



def gen_random1(num_count, begin, end):
    while num_count > 0:
        yield random.randint(begin, end) #сохраняет состояние функции до сл вызова
        num_count -= 1

'''
print(gen_random(5, 1, 3), '   ')
for i in gen_random(5,1,3):
    print(i)
'''
