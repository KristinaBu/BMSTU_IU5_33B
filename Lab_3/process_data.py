import json
import sys
from print_result import print_result
import cm_timer
from unique import Unique
import re
import gen_random
# Сделаем другие необходимые импорты

path = 'data_light.json'
#path = 'test_3.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

'''with open(path) as f:
    data = json.load(f)'''
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data[0])

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return  [element for element in Unique([item["job-name"] for item in arg
            if "job-name" in item],ignore_case=True )]
@print_result
def f2(arg):
    return [x
            for x in arg
            if re.match("^программист",x) ]
@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    return [f"{e}, зарплата {y} руб." for e,y in zip(arg, gen_random.gen_random1(len(arg),100000,200000))]

if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
