import os
import tempfile

class File:
    index = 0
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return self.path
    
    def write(self, text):
        with open(self.path, 'a') as f:
            f.write(text)
    
    def __add__(self, object):
        with open(self.path, 'r') as f1:
            with open(object.path, 'r') as f2:
                save = os.path.join(tempfile.gettempdir(), 'tmp.txt')
                new_obj = File(save)
                with open(save, 'w') as f:
                    f.write(f1.read())
                    f.write(f2.read())
                    return new_obj
    
    def __iter__(self):
        return self
    def __next__(self):
        with open(self.path, 'r') as f:
            if self.index >= os.path.getsize(self.path):
                raise StopIteration
            f.seek(self.index)
            tmp = f.readline()
            self.index += len(tmp)
            return tmp
