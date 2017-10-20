# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
from time import time

import contextlib
@contextlib.contextmanager
def timer():
    t1 = time()
    yield
    t2 = time()
    t=t2-t1
    print(t)
