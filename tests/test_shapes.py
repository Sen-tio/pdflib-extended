from pdflib_extended.pdflib import PDFlib
from pdflib_extended.extensions.classes import Box


def test_rectangle(new_page_scoped_pdflib_object: PDFlib):
    p: PDFlib = new_page_scoped_pdflib_object
    p_result = p.fit_rectangle(Box(0, 0, 1, 1))
    assert p_result >= 0
