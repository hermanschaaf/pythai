#include <Python.h>
#include "structmember.h"
#include <thai/thbrk.h>
#if PY_MAJOR_VERSION >= 3
static PyObject*
th_brk_(PyObject *self, PyObject *args) 
{
    PyObject *result = NULL;
    Py_UNICODE *s1;
    int s1_len;

    if (!PyArg_ParseTuple(args, "u#", &s1, &s1_len)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be unicode");
        return NULL;
    }

    if(s1_len == 0) {
        PyErr_SetString(PyExc_ValueError, "parameter must not be empty string");
        return NULL;
    }

    PyObject *txt_cp874 = PyUnicode_Encode(s1, s1_len, "CP874", NULL);
    if(txt_cp874 == NULL) {
        return NULL;
    }

    Py_ssize_t len = PyBytes_Size(txt_cp874);
    char *c_txt_cp874 = PyBytes_AsString(txt_cp874);
    int *pos = (int *)malloc(sizeof(int) * (s1_len + 1)); 
    int n = th_brk((unsigned char *)c_txt_cp874, pos, len);
    int i, s = 0;
    char *buffer;
    result = PyList_New(0);
    for(i = 0; i < n; i++) {
        PyObject *tok;
        PyObject *tok_cp874 = PySequence_GetSlice(txt_cp874, s, pos[i]);
        Py_ssize_t tok_len;
        PyBytes_AsStringAndSize(tok_cp874, &buffer, &tok_len);
        tok = PyUnicode_Decode(buffer, tok_len, "CP874", NULL);
        s = pos[i];
        PyList_Append(result, tok); 
        Py_XDECREF(tok_cp874);
        Py_XDECREF(tok);
    } 
    if(s < len) {
        PyObject *tok_cp874 = PySequence_GetSlice(txt_cp874, s, len);
        Py_ssize_t tok_len;
        PyObject *tok;
        PyBytes_AsStringAndSize(tok_cp874, &buffer, &tok_len);
        tok = PyUnicode_Decode(buffer, tok_len, "CP874", NULL);
        PyList_Append(result, tok);
        Py_XDECREF(tok_cp874);
        Py_XDECREF(tok);
    } 
    Py_XDECREF(txt_cp874);

    free(pos); 
    return result;
}

static PyMethodDef module_methods[] = {
    {"th_brk", (PyCFunction)th_brk_, METH_VARARGS,
     "Thai word break"},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,  /* m_base */
    "libthai",                 /* m_name */
    NULL,                   /* m_doc */
    -1,                     /* m_size */
    module_methods            /* m_methods */
};
PyMODINIT_FUNC
PyInit_libthai(void) 
{
    PyObject* m;
    m = PyModule_Create(&moduledef);
    if (m == NULL)
      return;
}
#else
	static PyObject*
th_brk_(PyObject *self, PyObject *args) 
{
    PyObject *result = NULL;
    Py_UNICODE *s1;
    int s1_len;

    if (!PyArg_ParseTuple(args, "u#", &s1, &s1_len)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be unicode");
        return NULL;
    }

    if(s1_len == 0) {
        PyErr_SetString(PyExc_ValueError, "parameter must not be empty string");
        return NULL;
    }

    PyObject *txt_cp874 = PyUnicode_Encode(s1, s1_len, "CP874", NULL);
    if(txt_cp874 == NULL) {
        return NULL;
    }

    Py_ssize_t len = PyString_Size(txt_cp874);
    char *c_txt_cp874 = PyString_AsString(txt_cp874);
    int *pos = (int *)malloc(sizeof(int) * (s1_len + 1)); 
    int n = th_brk((unsigned char *)c_txt_cp874, pos, len);
    int i, s = 0;
    char *buffer;
    result = PyList_New(0);
    for(i = 0; i < n; i++) {
        PyObject *tok;
        PyObject *tok_cp874 = PySequence_GetSlice(txt_cp874, s, pos[i]);
        Py_ssize_t tok_len;
        PyString_AsStringAndSize(tok_cp874, &buffer, &tok_len);
        tok = PyUnicode_Decode(buffer, tok_len, "CP874", NULL);
        s = pos[i];
        PyList_Append(result, tok); 
        Py_XDECREF(tok_cp874);
        Py_XDECREF(tok);
    } 
    if(s < len) {
        PyObject *tok_cp874 = PySequence_GetSlice(txt_cp874, s, len);
        Py_ssize_t tok_len;
        PyObject *tok;
        PyString_AsStringAndSize(tok_cp874, &buffer, &tok_len);
        tok = PyUnicode_Decode(buffer, tok_len, "CP874", NULL);
        PyList_Append(result, tok);
        Py_XDECREF(tok_cp874);
        Py_XDECREF(tok);
    } 
    Py_XDECREF(txt_cp874);

    free(pos); 
    return result;
}

static PyMethodDef module_methods[] = {
    {"th_brk", (PyCFunction)th_brk_, METH_VARARGS,
     "Thai word break"},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
initlibthai(void) 
{
    PyObject* m;
    m = Py_InitModule3("libthai", module_methods,
                       "libthai module");
    if (m == NULL)
      return;
}
#endif