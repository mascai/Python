from multiprocessing import Process

def f(name):
	print("Hello", name)

p = Process(target=f, args=("Bob",)) # функция, которую хочу исполнить и ее аргументы 
p.start() # вызов fork и работа дочернего 
p.join() # ожидаем завершения дочернего процесса

