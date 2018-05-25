''' Object stricture on C-level'''

typedef struct object {
	_PyObject_HEAD_EXTRA
	Py_ssize_t ob_refcnt;        // Reference counter
	struct _typeobject *ob_type; // Pointer to object type
} PyObject;

typedef struct {
	PyObject ob_base;
	Py_ssize_t ob_size; // Number of elements in variable part

} PyObject;

''' Macroses for type expansion '''

#define PyObject_HEAD PyObject ob_base;

'''
Практически все в Python наследуется от PyObject, является объектом и может быть присвоено переменной 
и быть передано в качестве аргумента в функцию! Не только базовые типы, такие как int, float, bool, str и т.д., 
но также и функции и даже модули, содержащие наш код на Python.

'''