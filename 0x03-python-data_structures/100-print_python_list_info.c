#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *obj;

	i = 0;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	while (i < size)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i += 1;
	}
}
