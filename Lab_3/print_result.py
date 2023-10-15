# Здесь должна быть реализация декоратора

def print_result1(func):
    def wrapper():

        print(func.__name__)
        res = func()
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for k in res:
                print(f'{k} = {res[k]}')
        else:
            print(res)
        return res
    return wrapper


def print_result(func):
    def wrapper(arg):

        res = func(arg)
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for k in res:
                print(f'{k} = {res[k]}')
        else:
            print(res)

        return res
    return wrapper

@print_result1
def test_1():
    return 1


@print_result1
def test_2():
    return 'iu5'


@print_result1
def test_3():
    return {'a': 1, 'b': 2}


@print_result1
def test_4():
    return [1, 2]


'''if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()'''