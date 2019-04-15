wbxmlbindingsdir = $(pyexecdir)
wbxmlbindings_LTLIBRARIES = pywbxml.la

pywbxml_la_CFLAGS = @PYTHON_INCLUDES@ @WBXML2_CFLAGS@
pywbxml_la_LDFLAGS = -module -avoid-version -fPIC @WBXML2_LIBS@
nodist_pywbxml_la_SOURCES = pywbxml.c

EXTRA_DIST = types.pxi pywbxml.pyx

CLEANFILES = pywbxml.c

pywbxml.c: $(srcdir)/types.pxi $(srcdir)/pywbxml.pyx
	pyrexc $(srcdir)/pywbxml.pyx -o ./pywbxml.c
