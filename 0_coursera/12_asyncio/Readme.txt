'''
Модуль select

-- Используется для организации неблокирующего ввода вывода
-- Для этого производит опрос файловых дескрипторов

В современных ОС Linux используют epoll.
При помощи вызова epoll.poll можно получить файловые дескрипторы готовые для чтения или записи.
Такой код иногда называют асинхронным программированием, 
или мультиплексирование ввода/вывода.
Пример сделан с целью обучения для понимания того как использовать неблокирующий ввод/вывод.

'''

mport socket
import select

# server

sock = socket.socket()
sock.bind(("", 10001)) # server on localhost 
sock.listen() 

# как обработать запросы для conn1 и conn2
# одновременно без потоков?
conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0) # неблокирующий режим
conn2.setblocking(0)
    
epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}

# Неблокирующий ввод/вывод, обучающий пример
# Цикл обработки событий в epoll

while True:
    events = epoll.poll(1)
    
    for fileno, event in events: # обработка поступивших событий
        if event & select.EPOLLIN:
            # обработка чтения из сокета
            data=conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))