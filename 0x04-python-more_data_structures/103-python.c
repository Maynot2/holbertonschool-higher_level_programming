#include "Python.h"
#include <stdio.h>
#include <string.h>

void print_bytes(PyBytesObject *pbo, Py_ssize_t size)
{
	Py_ssize_t i = 0;

	for (i = 0; i <= size; i++)
		printf(" %02x", (uint8_t)pbo->ob_sval[i]);
	puts("");
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbo = (PyBytesObject *)p;
	Py_ssize_t size =  (((PyVarObject *)(p))->ob_size);
	Py_ssize_t print_size =  size < 10 ? size : 9;

	puts("[.] bytes object info");
	if (strcmp("bytes", p->ob_type->tp_name) == 0)
	{
		printf(" size: %lu\n", size);
		printf(" trying string: %s\n", pbo->ob_sval);
		printf(" first %lu bytes:", print_size + 1);
		print_bytes(pbo, print_size);
	}
	else
	{
		puts(" [ERROR] Invalid Bytes Object");
	}

}

/**
 * print_python_list_info - Prints info about python
 * @p: A Pyobject
 *
 * Return: Nothing.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	PyObject *el;
	Py_ssize_t i;
	const char *name;

	size = ((PyVarObject *)(p))->ob_size;
	puts("[*] Python list info");
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
	i = 0;
	while (i < size)
	{
		el = ((PyListObject *)p)->ob_item[i];
		name = (((PyObject *)(el))->ob_type)->tp_name;
		printf("Element %lu: %s\n", i, name);
		if (strcmp(name, "bytes") == 0)
			print_python_bytes(el);
		++i;
	}
}
