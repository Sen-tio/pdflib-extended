from pdflib_extended.pdflib import PDFlib
from pdflib_extended.extensions.classes import Box


def test_text_box(new_page_scoped_pdflib_object):
    p: PDFlib = new_page_scoped_pdflib_object
    p_result: str = p.fit_text_box("Hello World", Box(0, 0, 1, 1))
    assert p_result == "_stop"
