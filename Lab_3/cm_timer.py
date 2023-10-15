import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f"Time: {self.interval} sec")
print("1st")
# Использование контекстного менеджера

'''with cm_timer_1():
   time.sleep(5.5)'''

print("2nd")

@contextmanager
def cm_timer_2():
    start_t = time.time()
    yield #приостанавливает свое выполнение, передавая управление обратно в блок with
    end_t = time.time()
    print(f"Time: {end_t - start_t} sec")

'''with cm_timer_2():
   time.sleep(5.5)'''