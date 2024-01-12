#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int lenght_count, mem_alloc, index;
	PyObject *obj;

	lenght_count = Py_SIZE(p);
	mem_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", lenght_count);
	printf("[*] Allocated = %d\n", mem_alloc);

	for (index = 0; index < lenght_count; index++)
	{
		printf("Element %d: ", index);

		obj = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
