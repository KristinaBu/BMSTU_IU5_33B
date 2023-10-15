# Итератор для удаления дубликатов
import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items_iter = set()
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            try:
                current = next(self.items)
            except StopIteration:
                raise StopIteration
            if self.ignore_case and isinstance(current, str):
                current = current.lower()
            if current not in self.items_iter:
                self.items_iter.add(current)
                return current

    def __iter__(self):
        return self


'''
data_list = [
    {0: [1, 1, 1, 1, 1, 2, 2, 2, 2, 2] },
    {0: ["a","A","b","B","a","A","b","B"]},
    {1: ["a","A","b","B","a","A","b","B"]},
    {0 : gen_random.gen_random1(10, 1, 3) }
]

for data_dict in data_list:
    for key in data_dict:
        data = data_dict[key]
        unique_iterator = Unique(data, ignore_case=key)
        print(f"Unique elements for key {key}:")
        for element in unique_iterator:
            print(element)'''

