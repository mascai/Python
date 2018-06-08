from multiprocessing import Process

class NewProc(Process):
	def __init__(self, name): # передаю въодные параметры процесса
		super().__init__()
		self.name = name
	def run(self): # содержание процесса
		print("hello", self.name)

p = NewProc("Alex")
p.start()
p.join()
