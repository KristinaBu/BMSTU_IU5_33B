from operator import itemgetter

class Musician:
    """Музыкант"""

    def __init__(self, id, fio, sal, orch_id):
        if id < 0:
            raise ValueError("ID музыканта не может быть отрицательным")
        self.id = id
        self.fio = fio
        if sal < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.sal = sal
        if orch_id < 0:
            raise ValueError("ID орекстра не может быть отрицательным")
        self.orch_id = orch_id


class Orchestra:
    """Оркестр"""

    def __init__(self, id, name):
        if id < 0:
            raise ValueError("ID орекстра не может быть отрицательным")
        self.id = id
        self.name = name


class MusOrch:
    """
    'Музыканты Оркестра' для реализации
    связи многие-ко-многим
    """

    def __init__(self, orch_id, mus_id):
        if orch_id < 0:
            raise ValueError("ID орекстра не может быть отрицательным")
        if mus_id < 0:
            raise ValueError("ID музыканта не может быть отрицательным")
        self.orch_id = orch_id
        self.mus_id = mus_id


def task1(one_to_many):
    return sorted([(fio, sal, name) for fio, sal, name in one_to_many if fio.startswith('А')], key=itemgetter(2))


def task2(one_to_many, orchestras):
    res_12_unsorted = []
    for d in orchestras:
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_emps) > 0:
            d_sals = [sal for _, sal, _ in d_emps]
            d_sals_min = min(d_sals)
            res_12_unsorted.append((d.name, d_sals_min))
    return sorted(res_12_unsorted, key=itemgetter(1),)

def task3(many_to_many, orchestras):
    res_13 = {}
    sorted_many_to_many = sorted(many_to_many, key=itemgetter(0))
    for d in orchestras:
        d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
        d_emps_names = [x for x, _, _ in d_emps]
        res_13[d.name] = d_emps_names
    return res_13


def main():
    orchestras = [
        Orchestra(1, 'деревянные духовые'),
        Orchestra(2, 'медные духовые'),
        Orchestra(3, 'струнные смычковые'),
        Orchestra(4, 'ударные'),
        Orchestra(11, 'деревянные духовые (другое)'),
        Orchestra(22, 'медные духовые (другое)'),
        Orchestra(33, 'струнные смычковые (другое)'),
        Orchestra(44, 'ударные (другое)'),
    ]

    musicians = [
        Musician(1, 'Артамонов', 25000, 1),
        Musician(2, 'Петров', 35000, 2),
        Musician(3, 'Иваненко', 45000, 3),
        Musician(4, 'Иванов', 35000, 3),
        Musician(5, 'Сушкин', 25000, 4),
    ]

    musicians_orchestras = [
        MusOrch(1, 1),
        MusOrch(2, 2),
        MusOrch(3, 3),
        MusOrch(3, 4),
        MusOrch(4, 5),
        MusOrch(11, 1),
        MusOrch(22, 2),
        MusOrch(33, 3),
        MusOrch(33, 4),
        MusOrch(44, 5),
    ]

    one_to_many = [(e.fio, e.sal, d.name)
                   for d in orchestras
                   for e in musicians
                   if e.orch_id == d.id]

    many_to_many_temp = [(d.name, ed.orch_id, ed.mus_id)
                         for d in orchestras
                         for ed in musicians_orchestras
                         if d.id == ed.orch_id]

    many_to_many = [(e.fio, e.sal, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in musicians if e.id == emp_id]

    print('Задание 1')
    print(task1(one_to_many))

    print('\nЗадание 2')
    print(task2(one_to_many, orchestras))

    print('\nЗадание 3')
    print(task3(many_to_many, orchestras))


if __name__ == '__main__':
    main()
