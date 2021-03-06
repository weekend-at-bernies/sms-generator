/* Generated by Pyrex 0.9.8.5 on Wed Oct 17 16:05:35 2018 */

#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "structmember.h"
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#if PY_VERSION_HEX < 0x02050000
  typedef int Py_ssize_t;
  #define PY_SSIZE_T_MAX INT_MAX
  #define PY_SSIZE_T_MIN INT_MIN
  #define PyInt_FromSsize_t(z) PyInt_FromLong(z)
  #define PyInt_AsSsize_t(o)	PyInt_AsLong(o)
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
#endif
#ifdef __cplusplus
#define __PYX_EXTERN_C extern "C"
#else
#define __PYX_EXTERN_C extern
#endif
#include <math.h>
#include "stddef.h"
#include "wbxml.h"
#include "wbxml_errors.h"
#include "wbxml_conv.h"
#include "stdlib.h"


typedef struct {PyObject **p; int i; char *s; long n;} __Pyx_StringTabEntry; /*proto*/

static PyObject *__pyx_m;
static PyObject *__pyx_b;
static int __pyx_lineno;
static char *__pyx_filename;
static char **__pyx_f;

static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name); /*proto*/

static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb); /*proto*/

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t); /*proto*/

static PyObject *__Pyx_CreateClass(PyObject *bases, PyObject *dict, PyObject *name, char *modname); /*proto*/

static void __Pyx_AddTraceback(char *funcname); /*proto*/

/* Declarations from pywbxml */


/* Declarations from implementation of pywbxml */


static char __pyx_k1[] = "code";
static char __pyx_k2[] = "description";
static char __pyx_k3[] = "%s (%d)";
static char __pyx_k4[] = "WBXMLParseError";
static char __pyx_k5[] = "unicode";
static char __pyx_k6[] = "encode";
static char __pyx_k7[] = "utf-8";
static char __pyx_k8[] = "invalid string";
static char __pyx_k9[] = "__init__";
static char __pyx_k10[] = "__str__";

static PyObject *__pyx_n_WBXMLParseError;
static PyObject *__pyx_n___init__;
static PyObject *__pyx_n___str__;
static PyObject *__pyx_n_code;
static PyObject *__pyx_n_description;
static PyObject *__pyx_n_encode;
static PyObject *__pyx_n_unicode;

static PyObject *__pyx_k3p;
static PyObject *__pyx_k7p;
static PyObject *__pyx_k8p;

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_WBXMLParseError, 1, __pyx_k4, sizeof(__pyx_k4)},
  {&__pyx_n___init__, 1, __pyx_k9, sizeof(__pyx_k9)},
  {&__pyx_n___str__, 1, __pyx_k10, sizeof(__pyx_k10)},
  {&__pyx_n_code, 1, __pyx_k1, sizeof(__pyx_k1)},
  {&__pyx_n_description, 1, __pyx_k2, sizeof(__pyx_k2)},
  {&__pyx_n_encode, 1, __pyx_k6, sizeof(__pyx_k6)},
  {&__pyx_n_unicode, 1, __pyx_k5, sizeof(__pyx_k5)},
  {&__pyx_k3p, 0, __pyx_k3, sizeof(__pyx_k3)},
  {&__pyx_k7p, 0, __pyx_k7, sizeof(__pyx_k7)},
  {&__pyx_k8p, 0, __pyx_k8, sizeof(__pyx_k8)},
  {0, 0, 0, 0}
};



/* Implementation of pywbxml */

static PyObject *__pyx_f_7pywbxml_15WBXMLParseError___init__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_7pywbxml_15WBXMLParseError___init__ = {"__init__", (PyCFunction)__pyx_f_7pywbxml_15WBXMLParseError___init__, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_f_7pywbxml_15WBXMLParseError___init__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_code = 0;
  PyObject *__pyx_r;
  WBXMLError __pyx_1;
  PyObject *__pyx_2 = 0;
  static char *__pyx_argnames[] = {"self","code",0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "OO", __pyx_argnames, &__pyx_v_self, &__pyx_v_code)) return 0;
  Py_INCREF(__pyx_v_self);
  Py_INCREF(__pyx_v_code);

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":19 */
  if (PyObject_SetAttr(__pyx_v_self, __pyx_n_code, __pyx_v_code) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 19; goto __pyx_L1;}

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":20 */
  __pyx_1 = PyInt_AsUnsignedLongMask(__pyx_v_code); if (PyErr_Occurred()) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 20; goto __pyx_L1;}
  __pyx_2 = PyString_FromString(((char *)wbxml_errors_string(__pyx_1))); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 20; goto __pyx_L1;}
  if (PyObject_SetAttr(__pyx_v_self, __pyx_n_description, __pyx_2) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 20; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_2);
  __Pyx_AddTraceback("pywbxml.WBXMLParseError.__init__");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  Py_DECREF(__pyx_v_code);
  return __pyx_r;
}

static PyObject *__pyx_f_7pywbxml_15WBXMLParseError___str__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_7pywbxml_15WBXMLParseError___str__ = {"__str__", (PyCFunction)__pyx_f_7pywbxml_15WBXMLParseError___str__, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_f_7pywbxml_15WBXMLParseError___str__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  PyObject *__pyx_2 = 0;
  PyObject *__pyx_3 = 0;
  static char *__pyx_argnames[] = {"self",0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "O", __pyx_argnames, &__pyx_v_self)) return 0;
  Py_INCREF(__pyx_v_self);
  __pyx_1 = PyObject_GetAttr(__pyx_v_self, __pyx_n_description); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; goto __pyx_L1;}
  __pyx_2 = PyObject_GetAttr(__pyx_v_self, __pyx_n_code); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; goto __pyx_L1;}
  __pyx_3 = PyTuple_New(2); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; goto __pyx_L1;}
  PyTuple_SET_ITEM(__pyx_3, 0, __pyx_1);
  PyTuple_SET_ITEM(__pyx_3, 1, __pyx_2);
  __pyx_1 = 0;
  __pyx_2 = 0;
  __pyx_1 = PyNumber_Remainder(__pyx_k3p, __pyx_3); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; goto __pyx_L1;}
  Py_DECREF(__pyx_3); __pyx_3 = 0;
  __pyx_r = __pyx_1;
  __pyx_1 = 0;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_1);
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_3);
  __Pyx_AddTraceback("pywbxml.WBXMLParseError.__str__");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  return __pyx_r;
}

static PyObject *__pyx_f_7pywbxml_wbxml2xml(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_7pywbxml_wbxml2xml(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_wbxml = 0;
  WB_UTINY *__pyx_v_xml;
  WB_ULONG __pyx_v_xml_len;
  WBXMLGenXMLParams __pyx_v_params;
  PyObject *__pyx_v_retval;
  PyObject *__pyx_v_s;
  PyObject *__pyx_r;
  Py_ssize_t __pyx_1;
  PyObject *__pyx_2 = 0;
  int __pyx_3;
  PyObject *__pyx_4 = 0;
  PyObject *__pyx_5 = 0;
  static char *__pyx_argnames[] = {"wbxml",0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "O", __pyx_argnames, &__pyx_v_wbxml)) return 0;
  Py_INCREF(__pyx_v_wbxml);
  __pyx_v_retval = Py_None; Py_INCREF(Py_None);
  __pyx_v_s = Py_None; Py_INCREF(Py_None);

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":30 */
  __pyx_v_params.gen_type = WBXML_GEN_XML_CANONICAL;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":31 */
  __pyx_v_params.lang = WBXML_LANG_AIRSYNC;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":32 */
  __pyx_v_params.indent = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":33 */
  __pyx_v_params.keep_ignorable_ws = 1;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":35 */
  __pyx_1 = PyObject_Length(__pyx_v_wbxml); if (__pyx_1 == -1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 35; goto __pyx_L1;}
  __pyx_2 = PyLong_FromUnsignedLong(wbxml_conv_wbxml2xml_withlen(((WB_UTINY *)PyString_AsString(__pyx_v_wbxml)),__pyx_1,(&__pyx_v_xml),(&__pyx_v_xml_len),(&__pyx_v_params))); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 35; goto __pyx_L1;}
  Py_DECREF(__pyx_v_retval);
  __pyx_v_retval = __pyx_2;
  __pyx_2 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":36 */
  __pyx_2 = PyInt_FromLong(0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 36; goto __pyx_L1;}
  if (PyObject_Cmp(__pyx_v_retval, __pyx_2, &__pyx_3) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 36; goto __pyx_L1;}
  __pyx_3 = __pyx_3 != 0;
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  if (__pyx_3) {
    __pyx_2 = __Pyx_GetName(__pyx_m, __pyx_n_WBXMLParseError); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; goto __pyx_L1;}
    __pyx_4 = PyTuple_New(1); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; goto __pyx_L1;}
    Py_INCREF(__pyx_v_retval);
    PyTuple_SET_ITEM(__pyx_4, 0, __pyx_v_retval);
    __pyx_5 = PyObject_CallObject(__pyx_2, __pyx_4); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; goto __pyx_L1;}
    Py_DECREF(__pyx_2); __pyx_2 = 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    __Pyx_Raise(__pyx_5, 0, 0);
    Py_DECREF(__pyx_5); __pyx_5 = 0;
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; goto __pyx_L1;}
    goto __pyx_L2;
  }
  __pyx_L2:;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":39 */
  __pyx_2 = PyString_FromStringAndSize(((char *)__pyx_v_xml),__pyx_v_xml_len); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 39; goto __pyx_L1;}
  Py_DECREF(__pyx_v_s);
  __pyx_v_s = __pyx_2;
  __pyx_2 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":40 */
  free(__pyx_v_xml);

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":42 */
  Py_INCREF(__pyx_v_s);
  __pyx_r = __pyx_v_s;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_4);
  Py_XDECREF(__pyx_5);
  __Pyx_AddTraceback("pywbxml.wbxml2xml");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_retval);
  Py_DECREF(__pyx_v_s);
  Py_DECREF(__pyx_v_wbxml);
  return __pyx_r;
}

static PyObject *__pyx_f_7pywbxml_xml2wbxml(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_7pywbxml_xml2wbxml(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_xml = 0;
  char *__pyx_v_xml_raw;
  int __pyx_v_xml_raw_len;
  WB_UTINY *__pyx_v_bytes;
  WB_ULONG __pyx_v_size;
  WBXMLGenWBXMLParams __pyx_v_params;
  PyObject *__pyx_v_retval;
  PyObject *__pyx_v_s;
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  int __pyx_2;
  PyObject *__pyx_3 = 0;
  PyObject *__pyx_4 = 0;
  static char *__pyx_argnames[] = {"xml",0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "O", __pyx_argnames, &__pyx_v_xml)) return 0;
  Py_INCREF(__pyx_v_xml);
  __pyx_v_retval = Py_None; Py_INCREF(Py_None);
  __pyx_v_s = Py_None; Py_INCREF(Py_None);

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":51 */
  __pyx_v_params.wbxml_version = WBXML_VERSION_13;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":52 */
  __pyx_v_params.keep_ignorable_ws = 1;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":53 */
  __pyx_v_params.use_strtbl = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":54 */
  __pyx_v_params.produce_anonymous = 1;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":56 */
  __pyx_1 = __Pyx_GetName(__pyx_b, __pyx_n_unicode); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 56; goto __pyx_L1;}
  __pyx_2 = PyObject_IsInstance(__pyx_v_xml,__pyx_1); if (__pyx_2 == -1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 56; goto __pyx_L1;}
  Py_DECREF(__pyx_1); __pyx_1 = 0;
  if (__pyx_2) {
    __pyx_1 = PyObject_GetAttr(__pyx_v_xml, __pyx_n_encode); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 57; goto __pyx_L1;}
    __pyx_3 = PyTuple_New(1); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 57; goto __pyx_L1;}
    Py_INCREF(__pyx_k7p);
    PyTuple_SET_ITEM(__pyx_3, 0, __pyx_k7p);
    __pyx_4 = PyObject_CallObject(__pyx_1, __pyx_3); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 57; goto __pyx_L1;}
    Py_DECREF(__pyx_1); __pyx_1 = 0;
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    Py_DECREF(__pyx_v_xml);
    __pyx_v_xml = __pyx_4;
    __pyx_4 = 0;
    goto __pyx_L2;
  }
  __pyx_L2:;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":59 */
  __pyx_2 = (PyString_AsStringAndSize(__pyx_v_xml,(&__pyx_v_xml_raw),(&__pyx_v_xml_raw_len)) == (-1));
  if (__pyx_2) {
    __pyx_1 = PyTuple_New(1); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 60; goto __pyx_L1;}
    Py_INCREF(__pyx_k8p);
    PyTuple_SET_ITEM(__pyx_1, 0, __pyx_k8p);
    __pyx_3 = PyObject_CallObject(PyExc_TypeError, __pyx_1); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 60; goto __pyx_L1;}
    Py_DECREF(__pyx_1); __pyx_1 = 0;
    __Pyx_Raise(__pyx_3, 0, 0);
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 60; goto __pyx_L1;}
    goto __pyx_L3;
  }
  __pyx_L3:;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":62 */
  __pyx_4 = PyLong_FromUnsignedLong(wbxml_conv_xml2wbxml_withlen(((WB_UTINY *)__pyx_v_xml_raw),__pyx_v_xml_raw_len,(&__pyx_v_bytes),(&__pyx_v_size),(&__pyx_v_params))); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  Py_DECREF(__pyx_v_retval);
  __pyx_v_retval = __pyx_4;
  __pyx_4 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":63 */
  __pyx_1 = PyInt_FromLong(0); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 63; goto __pyx_L1;}
  if (PyObject_Cmp(__pyx_v_retval, __pyx_1, &__pyx_2) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 63; goto __pyx_L1;}
  __pyx_2 = __pyx_2 != 0;
  Py_DECREF(__pyx_1); __pyx_1 = 0;
  if (__pyx_2) {
    __pyx_3 = __Pyx_GetName(__pyx_m, __pyx_n_WBXMLParseError); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; goto __pyx_L1;}
    __pyx_4 = PyTuple_New(1); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; goto __pyx_L1;}
    Py_INCREF(__pyx_v_retval);
    PyTuple_SET_ITEM(__pyx_4, 0, __pyx_v_retval);
    __pyx_1 = PyObject_CallObject(__pyx_3, __pyx_4); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; goto __pyx_L1;}
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    __Pyx_Raise(__pyx_1, 0, 0);
    Py_DECREF(__pyx_1); __pyx_1 = 0;
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; goto __pyx_L1;}
    goto __pyx_L4;
  }
  __pyx_L4:;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":66 */
  __pyx_3 = PyString_FromStringAndSize(((char *)__pyx_v_bytes),__pyx_v_size); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 66; goto __pyx_L1;}
  Py_DECREF(__pyx_v_s);
  __pyx_v_s = __pyx_3;
  __pyx_3 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":67 */
  free(__pyx_v_bytes);

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":69 */
  Py_INCREF(__pyx_v_s);
  __pyx_r = __pyx_v_s;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_1);
  Py_XDECREF(__pyx_3);
  Py_XDECREF(__pyx_4);
  __Pyx_AddTraceback("pywbxml.xml2wbxml");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_retval);
  Py_DECREF(__pyx_v_s);
  Py_DECREF(__pyx_v_xml);
  return __pyx_r;
}

static struct PyMethodDef __pyx_methods[] = {
  {"wbxml2xml", (PyCFunction)__pyx_f_7pywbxml_wbxml2xml, METH_VARARGS|METH_KEYWORDS, 0},
  {"xml2wbxml", (PyCFunction)__pyx_f_7pywbxml_xml2wbxml, METH_VARARGS|METH_KEYWORDS, 0},
  {0, 0, 0, 0}
};

static void __pyx_init_filenames(void); /*proto*/

PyMODINIT_FUNC initpywbxml(void); /*proto*/
PyMODINIT_FUNC initpywbxml(void) {
  PyObject *__pyx_1 = 0;
  PyObject *__pyx_2 = 0;
  PyObject *__pyx_3 = 0;
  PyObject *__pyx_4 = 0;
  __pyx_init_filenames();
  __pyx_m = Py_InitModule4("pywbxml", __pyx_methods, 0, 0, PYTHON_API_VERSION);
  if (!__pyx_m) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; goto __pyx_L1;};
  Py_INCREF(__pyx_m);
  __pyx_b = PyImport_AddModule("__builtin__");
  if (!__pyx_b) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; goto __pyx_L1;};
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; goto __pyx_L1;};
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; goto __pyx_L1;};

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":17 */
  __pyx_1 = PyDict_New(); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; goto __pyx_L1;}
  __pyx_2 = PyTuple_New(0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; goto __pyx_L1;}
  __pyx_3 = __Pyx_CreateClass(__pyx_2, __pyx_1, __pyx_n_WBXMLParseError, "pywbxml"); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":18 */
  __pyx_2 = PyCFunction_New(&__pyx_mdef_7pywbxml_15WBXMLParseError___init__, 0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 18; goto __pyx_L1;}
  __pyx_4 = PyMethod_New(__pyx_2, 0, __pyx_3); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 18; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  if (PyObject_SetAttr(__pyx_3, __pyx_n___init__, __pyx_4) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 18; goto __pyx_L1;}
  Py_DECREF(__pyx_4); __pyx_4 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":22 */
  __pyx_2 = PyCFunction_New(&__pyx_mdef_7pywbxml_15WBXMLParseError___str__, 0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 22; goto __pyx_L1;}
  __pyx_4 = PyMethod_New(__pyx_2, 0, __pyx_3); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 22; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  if (PyObject_SetAttr(__pyx_3, __pyx_n___str__, __pyx_4) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 22; goto __pyx_L1;}
  Py_DECREF(__pyx_4); __pyx_4 = 0;
  if (PyObject_SetAttr(__pyx_m, __pyx_n_WBXMLParseError, __pyx_3) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; goto __pyx_L1;}
  Py_DECREF(__pyx_3); __pyx_3 = 0;
  Py_DECREF(__pyx_1); __pyx_1 = 0;

  /* "/media/isa/aesop/droppy/Dropbox/alig/imran/code/git/sms-generator/pywbxml-0.1/0.1/src/pywbxml.pyx":44 */
  return;
  __pyx_L1:;
  Py_XDECREF(__pyx_1);
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_3);
  Py_XDECREF(__pyx_4);
  __Pyx_AddTraceback("pywbxml");
}

static char *__pyx_filenames[] = {
  "pywbxml.pyx",
};

/* Runtime support code */

static void __pyx_init_filenames(void) {
  __pyx_f = __pyx_filenames;
}

static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name) {
    PyObject *result;
    result = PyObject_GetAttr(dict, name);
    if (!result)
        PyErr_SetObject(PyExc_NameError, name);
    return result;
}

static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb) {
    Py_XINCREF(type);
    Py_XINCREF(value);
    Py_XINCREF(tb);
    /* First, check the traceback argument, replacing None with NULL. */
    if (tb == Py_None) {
        Py_DECREF(tb);
        tb = 0;
    }
    else if (tb != NULL && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto raise_error;
    }
    /* Next, replace a missing value with None */
    if (value == NULL) {
        value = Py_None;
        Py_INCREF(value);
    }
    #if PY_VERSION_HEX < 0x02050000
    if (!PyClass_Check(type))
    #else
    if (!PyType_Check(type))
    #endif
    {
        /* Raising an instance.  The value should be a dummy. */
        if (value != Py_None) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        /* Normalize to raise <class>, <instance> */
        Py_DECREF(value);
        value = type;
        #if PY_VERSION_HEX < 0x02050000
            if (PyInstance_Check(type)) {
                type = (PyObject*) ((PyInstanceObject*)type)->in_class;
                Py_INCREF(type);
            }
            else {
                PyErr_SetString(PyExc_TypeError,
                    "raise: exception must be an old-style class or instance");
                goto raise_error;
            }
        #else
            type = (PyObject*) type->ob_type;
            Py_INCREF(type);
            if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
                PyErr_SetString(PyExc_TypeError,
                    "raise: exception class must be a subclass of BaseException");
                goto raise_error;
            }
        #endif
    }
    PyErr_Restore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        if (!*t->p)
            return -1;
        if (t->i)
            PyString_InternInPlace(t->p);
        ++t;
    }
    return 0;
}

static PyObject *__Pyx_CreateClass(
    PyObject *bases, PyObject *dict, PyObject *name, char *modname)
{
    PyObject *py_modname;
    PyObject *result = 0;
    
    py_modname = PyString_FromString(modname);
    if (!py_modname)
        goto bad;
    if (PyDict_SetItemString(dict, "__module__", py_modname) < 0)
        goto bad;
    result = PyClass_New(bases, dict, name);
bad:
    Py_XDECREF(py_modname);
    return result;
}

#include "compile.h"
#include "frameobject.h"
#include "traceback.h"

static void __Pyx_AddTraceback(char *funcname) {
    PyObject *py_srcfile = 0;
    PyObject *py_funcname = 0;
    PyObject *py_globals = 0;
    PyObject *empty_tuple = 0;
    PyObject *empty_string = 0;
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    
    py_srcfile = PyString_FromString(__pyx_filename);
    if (!py_srcfile) goto bad;
    py_funcname = PyString_FromString(funcname);
    if (!py_funcname) goto bad;
    py_globals = PyModule_GetDict(__pyx_m);
    if (!py_globals) goto bad;
    empty_tuple = PyTuple_New(0);
    if (!empty_tuple) goto bad;
    empty_string = PyString_FromString("");
    if (!empty_string) goto bad;
    py_code = PyCode_New(
        0,            /*int argcount,*/
        0,            /*int nlocals,*/
        0,            /*int stacksize,*/
        0,            /*int flags,*/
        empty_string, /*PyObject *code,*/
        empty_tuple,  /*PyObject *consts,*/
        empty_tuple,  /*PyObject *names,*/
        empty_tuple,  /*PyObject *varnames,*/
        empty_tuple,  /*PyObject *freevars,*/
        empty_tuple,  /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        __pyx_lineno,   /*int firstlineno,*/
        empty_string  /*PyObject *lnotab*/
    );
    if (!py_code) goto bad;
    py_frame = PyFrame_New(
        PyThreadState_Get(), /*PyThreadState *tstate,*/
        py_code,             /*PyCodeObject *code,*/
        py_globals,          /*PyObject *globals,*/
        0                    /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    py_frame->f_lineno = __pyx_lineno;
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_srcfile);
    Py_XDECREF(py_funcname);
    Py_XDECREF(empty_tuple);
    Py_XDECREF(empty_string);
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}
