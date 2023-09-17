import math
import sys

class Sq_Roots:
    """Класс коэффициентов"""
    def __init__(self):
        self.A = 0.0
        self.B = 0.0
        self.C = 0.0
        self.root_list = set()

    def check_root(self, ind):
        """Проверка коэфов"""
        try:
            global coef
            coef = sys.argv[ind]
        except:
            print("Введите коэффициент {} :".format(ind) )
            coef = input()
            #Проверка А на ноль(иначе впоследствие ошибка в делении на ноль)
            if float(coef) == 0.0 and ind == 1:
                print("Коэффициент 1 равен 0. Введите отличное от 0 число.")
                self.check_root(1)
        return float(coef)

    def get_roots(self):
        """Получение значений коэфов"""
        self.A = self.check_root(1)
        self.B = self.check_root(2)
        self.C = self.check_root(3)

    def calculation(self):
        """Подсчет корней"""
        #Дискриминант
        D = self.B**2 - 4*self.A*self.C
        if (D>=0):
            self.root_list.add( (-self.B + math.sqrt(D))/ (2*self.A) )
            self.root_list.add( (-self.B - math.sqrt(D))/ (2*self.A) )

    def print_ans(self):
        """Вывод ответов"""
        if len(self.root_list)==0:
            print("Нет корней, дискриминант меньше нуля :(")
            return
        print("Корни:")
        for e in self.root_list:
            print(e, " ")

def main():
    """Основная функция"""
    sr = Sq_Roots()
    sr.get_roots()
    sr.calculation()
    sr.print_ans()

if __name__ == "__main__":
    main()