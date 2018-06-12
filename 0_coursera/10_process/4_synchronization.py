# Синхронизация потоков, блокировки

import threading

class Point(object):
    def __init__(self, x, y):
        self.mutex = threading.RLock()
        self.set(x, y)

    def get(self):
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        with self.mutex:
            self.x = x
            self.y = y

# use in threads
my_point = Point(10, 20)
my_point.set(15, 10)
my_point.get()


'''
Этот код гарантирует что если объект класса Point будет использоваться в разных потоках,
то изменение x и y будет всегда атомарным.

Работает все это так: - при вызове метода берем блокировку через with self._mutex
Весь код внутри with блока будет выполнятся только в одном потоке.

Другими словами, если два разных потока вызовут .get то пока первый поток не выйдет из блока 
второй будет его ждать - и только потом продолжит выполнение.

Зачем это все нужно? Координаты нужно менять одновременно - ведь точка это атомарный объект.
Если позволить одному потоку поменять x, а другой в это же время поправит y
логика алгоритма может сломаться.

'''