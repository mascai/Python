''' Декораторы — это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.
    Декоратор - это функция, которая принимает функцию и возвращает функцию
'''

def decorator(func): # простейшая функия, которая принимает ф-цию и возвращает ее
	return func

@decorator
def decorated(a, b):
	return a * b
# decorated = decorator(decorated) - вот так работает декоратор

#print(decorated(5, 10))

##############################################################

def logger(func):
    def wrapped(*args, **kwargs): # обертка над функцией, которая записывает результаты работы в файл
        res = func(*args, **kwargs)
        with open("log.txt", 'w') as f:
            f.write(str(res))
        return res	
    return wrapped

@logger
def summator(vec):
	return sum(vec)

print("Summator: {}".format(summator([1, 2, 3, 4, 5]))) # 15

with open("log.txt", 'r') as f:
	print("log.txt: {}".format(f.read())) # 15