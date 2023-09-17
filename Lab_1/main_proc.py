import math
import sys

def check_root(ind):
    """Проверка коэфов -> возвращает один коэф"""
    try:
        global coef
        coef = sys.argv[ind]
    except:
        print("Введите коэффициент {} :".format(ind) )
        coef = input()
        #Проверка А на ноль(иначе впоследствие ошибка в делении на ноль)
        if float(coef) == 0.0 and ind == 1:
            print("Коэффициент 1 равен 0. Так не пойдет")
            check_root(1)
    return float(coef)

def get_roots(coef_list):
    """Получение значений коэфов -> возвращает список коэфов"""
    for i in range(0,3):
        coef_list[i] = check_root(i+1)
    return coef_list

def calculation(coef_list):
    """Подсчет корней -> возвращает множество корней"""
    A = coef_list[0]
    B = coef_list[1]
    C = coef_list[2]
    #Дискриминант
    D = B**2 - 4*A*C
    #Корни
    root_list = set()
    if (D>=0):
        root_list.add( (-B + math.sqrt(D))/ (2*A) )
        root_list.add( (-B - math.sqrt(D))/ (2*A) )
    return root_list

def print_ans(root_list):
    """Вывод ответов"""
    if len(root_list) == 0:
        print("Нет корней, дискриминант меньше нуля :(")
        return
    print("Корни:")
    for e in root_list:
        print(e, " ")

def all_process(coef_list):
    """Запускает последовательно все функции"""
    print_ans(calculation(get_roots(coef_list)))

def main():
    """Основная функция"""
    coef_list = [0.0]*3
    all_process(coef_list)

if __name__ == "__main__":
    main()