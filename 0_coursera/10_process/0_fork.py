import time
import os

pid = os.fork()
if pid == 0:
	# daughter
	print("child: ", os.getpid())
	time.sleep(2)
else:
	print("parent", os.getpid())
	os.wait()
	
