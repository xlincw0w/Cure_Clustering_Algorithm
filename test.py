from threading import Thread
from multiprocessing import Process


class A:
    def func1(x):
        for i in range(0, 50000):
            print('func1', i)

    def func2(x):
        for i in range(0, 50000):
            print('func2', i)


if __name__ == '__main__':

    print('Khaled')

    Th1 = Process(target=A.func1, args=(5, ))
    Th2 = Process(target=A.func2, args=(3, ))
    Th1.start()
    Th2.start()
    Th1.join()
    Th2.join()

    print('2')