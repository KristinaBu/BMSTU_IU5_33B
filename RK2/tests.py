import unittest
from main import *


class TestMusician(unittest.TestCase):
    """Тестовый класс для класса Musician"""

    def test_Musician(self):
        """Тестирование конструктора класса Musician"""
        m = Musician(1, 'F I O', 0, 2)
        self.assertEqual(m.id, 1)  # Проверка id
        self.assertEqual(m.fio, 'F I O')  # Проверка ФИО
        self.assertEqual(m.sal, 0)  # Проверка зарплаты
        self.assertEqual(m.orch_id, 2)  # Проверка id оркестра

    def test_negative_salary(self):
        """Тестирование конструктора класса Musician с отрицательной зарплатой"""
        with self.assertRaises(ValueError) as e:
            m = Musician(1, 'Иванов', -1000, 1)
        self.assertEqual(str(e.exception), "Зарплата не может быть отрицательной")

    def test_negative_id(self):
        """Тестирование конструктора класса Musician с отрицательным id"""
        with self.assertRaises(ValueError) as e:
            m = Musician(-1, 'Иванов', 1000, 1)
        self.assertEqual(str(e.exception), "ID музыканта не может быть отрицательным")

    def test_negative_orch_id(self):
        """Тестирование конструктора класса Musician с отрицательным id оркестра"""
        with self.assertRaises(ValueError) as e:
            m = Musician(1, 'Иванов', 1000, -1)
        self.assertEqual(str(e.exception), "ID орекстра не может быть отрицательным")


class TestOrchestra(unittest.TestCase):
    """Тестовый класс для класса Orchestra"""

    def test_Orchestra(self):
        """Тестирование конструктора класса Orchestra"""
        o = Orchestra(1, 'Bublik')
        self.assertEqual(o.id, 1)  # Проверка id
        self.assertEqual(o.name, 'Bublik')  # Проверка названия

    def test_negative_id(self):
        """Тестирование конструктора класса Orchestra с отрицательным id"""
        with self.assertRaises(ValueError) as e:
            o = Orchestra(-1, 'Струнные')
        self.assertEqual(str(e.exception), "ID орекстра не может быть отрицательным")


class TestMusOrch(unittest.TestCase):
    """Тестовый класс для класса MusOrch"""

    def test_MusOrch(self):
        """Тестирование конструктора класса MusOrch"""
        mo = MusOrch(3, 5)
        self.assertEqual(mo.orch_id, 3)  # Проверка id оркестра
        self.assertEqual(mo.mus_id, 5)  # Проверка id музыканта

    def test_negative_orch_id(self):
        """Тестирование конструктора класса MusOrch с отрицательным id оркестра"""
        with self.assertRaises(ValueError) as e:
            mo = MusOrch(-1, 1)
        self.assertEqual(str(e.exception), "ID орекстра не может быть отрицательным")

    def test_negative_mus_id(self):
        """Тестирование конструктора класса MusOrch с отрицательным id музыканта"""
        with self.assertRaises(ValueError) as e:
            mo = MusOrch(1, -1)
        self.assertEqual(str(e.exception), "ID музыканта не может быть отрицательным")


class TestTasks(unittest.TestCase):
    """Тестовый класс для функций task1, task2 и task3"""

    def test_1(self):
        """Тестирование функции task1"""
        right = [('Артамонов', 25000, 'деревянные духовые')]
        self.assertEqual('foo'.upper(), 'FOO')

    def test_2(self):
        """Тестирование функции task2"""
        right = [('деревянные духовые', 25000), ('ударные', 25000), ('медные духовые', 35000),
                 ('струнные смычковые', 35000)]
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_3(self):
        """Тестирование функции task3"""
        right = {'деревянные духовые': ['Артамонов'],
                 'медные духовые': ['Петров'],
                 'струнные смычковые': ['Иваненко', 'Иванов'],
                 'ударные': ['Сушкин'],
                 'деревянные духовые (другое)': ['Артамонов'],
                 'медные духовые (другое)': ['Петров'],
                 'струнные смычковые (другое)': ['Иваненко', 'Иванов'],
                 'ударные (другое)': ['Сушкин']}

if __name__ == '__main__':
    unittest.main()