#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Prints info about python
 * @p: A Pyobject
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;
	PyObject *elem;
	Py_ssize_t i;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
	i = 0;
	while (i < len)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %lu: %s\n", i, Py_TYPE(elem)->tp_name);
		++i;
	}
}
