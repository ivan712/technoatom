#include <Python.h>

PyObject *get_el(PyObject *self, PyObject *args)
{
	
	PyObject *list;
	PyObject *el;	
	
	if (!PyArg_ParseTuple(args, "OO", &list,&el))
    		{
        		return NULL;
    		}
	int n = PyInt_AsLong(PyTuple_GetItem(el,0));
	int m = PyInt_AsLong(PyTuple_GetItem(el,1));
		

	return PyList_GetItem(PyList_GetItem(list,n),m);
	
		
}




PyObject *in_matrix(PyObject *self, PyObject *args){
	
	PyObject *list;
	int el;	
	
	if (!PyArg_ParseTuple(args, "Oi", &list,&el))
    		{
        		return NULL;
    		}
	int n = PyList_Size(list);
	int m = PyList_Size(PyList_GetItem(list,0));
	
	for (int i=0; i<n; i++){
		for (int j=0; j<m; j++){
			if (PyInt_AsLong(PyList_GetItem(PyList_GetItem(list,i),j))==el)
				return Py_True;		
		

		}
	}
	return Py_False;
	
		
}




PyObject *tranc_mat(PyObject *self, PyObject *args)
{

	PyObject *list1;
	

	if (!PyArg_ParseTuple(args, "O", &list1))
    		{
        		return NULL;
    		}

	int n = PyList_Size(list1);
	int m = PyList_Size(PyList_GetItem(list1,0));
	
	PyObject *row = PyList_New(n);
	PyObject *res = PyList_New(m);
	int el;
	for (int i=0; i<m; i++){
		for (int j=0; j<n; j++){
			el = PyInt_AsLong(PyList_GetItem(PyList_GetItem(list1,j),i));	
			PyList_SetItem(row,j,Py_BuildValue("i",el));
		}	
		PyList_SetItem(res,i,row);
		row = PyList_New(n);
	}	
	return res;

}


PyObject *div_koef(PyObject *self, PyObject *args)
{

	PyObject *list1;
	double k;

	if (!PyArg_ParseTuple(args, "Od", &list1, &k))
    		{
        		return NULL;
    		}

	int n = PyList_Size(list1);
	int m = PyList_Size(PyList_GetItem(list1,0));
	
	PyObject *row = PyList_New(0);
	PyObject *res = PyList_New(0);
	double el = 0;
	for (int i=0; i<n; i++){
		for (int j = 0; j<m; j++){
			
			el = (double)PyInt_AsLong(PyList_GetItem(PyList_GetItem(list1,i),j))/k;	

				 	
			
			PyList_Append(row,Py_BuildValue("d",el));
			
		}
		PyList_Append(res,row);
		row = PyList_New(0);
	}

	return res;

}

PyObject *sum_mat(PyObject *self, PyObject *args)
{

	PyObject *list1;
	PyObject *list2;
	
	if (!PyArg_ParseTuple(args, "OO", &list1, &list2))
    {
        return NULL;
    }
	int n = PyList_Size(list1);
	int m = PyList_Size(PyList_GetItem(list2,0));
	
	PyObject *row = PyList_New(0);
	PyObject *res = PyList_New(0);
	int el = 0;
	for (int i=0; i<n; i++){
		for (int j = 0; j<m; j++){
			
			el += PyInt_AsLong(PyList_GetItem(PyList_GetItem(list1,i),j))+
			PyInt_AsLong(PyList_GetItem(PyList_GetItem(list2,i),j));	

				 	
			
			PyList_Append(row,Py_BuildValue("i",el));
			el = 0;
		}
		PyList_Append(res,row);
		row = PyList_New(0);
	}

	return res;

}



PyObject *mult_mat(PyObject *self, PyObject *args)
{

	PyObject *list1;
	PyObject *list2;
	
	if (!PyArg_ParseTuple(args, "OO", &list1, &list2))
    {
        return NULL;
    }
	int n = PyList_Size(list1);
	int v = PyList_Size(list2);
	int m = PyList_Size(PyList_GetItem(list2,0));
	
	PyObject *row = PyList_New(0);
	PyObject *res = PyList_New(0);
	int el = 0;
	for (int i=0; i<n; i++){
		for (int j = 0; j<m; j++){
			for (int k = 0; k<v; k++){
				el += PyInt_AsLong(PyList_GetItem(PyList_GetItem(list1,i),k))*
				      PyInt_AsLong(PyList_GetItem(PyList_GetItem(list2,k),j));	

				 	
			}
			PyList_Append(row,Py_BuildValue("i",el));
			el = 0;
		}
		PyList_Append(res,row);
		row = PyList_New(0);
	}

	return res;

}


 
PyObject *mult_koef( PyObject *self, PyObject *args)
{
    
    PyObject *list_obj_1;
    PyObject *matrix = PyList_New(0);
    PyObject *row = PyList_New(0);
	
    //PyObject *list_obj_2;
    int n,m,koeff;
    if (!PyArg_ParseTuple(args, "Oi", &list_obj_1,&koeff))
    {
        return NULL;
    }
 	
    n = PyList_Size(list_obj_1);	
    m = PyList_Size(PyList_GetItem(list_obj_1,0));
    
    for (int i = 0; i<n; i++){
	for (int j=0; j<m; j++){
		PyObject *Append = Py_BuildValue("i",PyInt_AsLong(PyList_GetItem(PyList_GetItem(list_obj_1,i),j))*koeff);
		PyList_Append(row, Append);
	
	}	
	PyList_Append(matrix, row);
        row = PyList_New(0);
}   
    return matrix;
}
 
 
static PyMethodDef example_methods[] = 
{
    { "mult_koef", (PyCFunction) mult_koef, METH_VARARGS, NULL },
    { "mult_mat", (PyCFunction) mult_mat, METH_VARARGS, NULL},
    { "sum_mat", (PyCFunction) sum_mat, METH_VARARGS, NULL},
    { "div_koef", (PyCFunction) div_koef, METH_VARARGS, NULL},
    { "tranc_mat", (PyCFunction) tranc_mat, METH_VARARGS, NULL},
    { "in_matrix", (PyCFunction) in_matrix, METH_VARARGS, NULL},	
    { "get_el", (PyCFunction) get_el, METH_VARARGS, NULL},
    { NULL, 0, 0, NULL }
};
 
 
PyMODINIT_FUNC initcmatrix()
{
   (void) Py_InitModule("example", example_methods);
 
    if (PyErr_Occurred())
    {
        PyErr_SetString(PyExc_ImportError, "example module init failed");
    }

}
