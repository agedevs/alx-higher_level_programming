#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int index;
	char *teststr = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", teststr);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (index = 0; index <= size && index < 10; index++)
		printf(" %02hhx", teststr[index]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int index;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (index = 0; index < size; index++)
        {
                type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", index, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[index]);
        }
}
