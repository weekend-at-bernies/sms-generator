dnl Process this file with autoconf to produce a configure script.
AC_PREREQ(2.53)
AC_INIT(pywbxml, 0.1)
AC_CONFIG_SRCDIR(README)
AM_INIT_AUTOMAKE(AC_PACKAGE_NAME, AC_PACKAGE_VERSION)

AM_MAINTAINER_MODE
AC_PROG_MAKE_SET

dnl Libtool.
AM_PROG_LIBTOOL

dnl Check for programs.
AC_PROG_CC
AC_PROG_INSTALL

dnl Check for libraries.
PKG_CHECK_MODULES(WBXML2, libwbxml2 >= 0.9.2)

dnl Check for header files.
AC_STDC_HEADERS

dnl Check for python and pyrex.
required_python_version=2.4
AM_PATH_PYTHON()

if test -z "$PYTHON"; then
    AC_MSG_ERROR([Python not found])
fi

AC_MSG_CHECKING([whether $PYTHON version >= $required_python_version])
AM_PYTHON_CHECK_VERSION([$PYTHON], [$required_python_version],
                      [AC_MSG_NOTICE([ok])],
                      [AC_MSG_ERROR([too old])])

AC_CHECK_PROGS(PYREX, pyrexc)
if test -z "$PYREX"; then
    AC_MSG_ERROR([Pyrex not found])
fi

AM_CHECK_PYTHON_HEADERS(AC_MSG_NOTICE([found]), AC_MSG_ERROR([not found]))

AC_OUTPUT([
Makefile
src/Makefile
tests/Makefile
])
