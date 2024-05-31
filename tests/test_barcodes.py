from pdflib_extended.extensions.classes import Point, Box
from pdflib_extended.pdflib import PDFlib


def test_datamatrix(new_page_scoped_pdflib_object: PDFlib) -> None:
    p: PDFlib = new_page_scoped_pdflib_object
    p_result: int = p.fit_datamatrix("1".zfill(6), Point(1, 1))
    assert p_result >= 0


def test_code_128(new_page_scoped_pdflib_object: PDFlib) -> None:
    p: PDFlib = new_page_scoped_pdflib_object
    p_result: int = p.fit_code_128_barcode("123123", Box(0, 0, 1, 1))
    assert p_result >= 0


def test_omr(new_page_scoped_pdflib_object: PDFlib) -> None:
    p: PDFlib = new_page_scoped_pdflib_object
    p_result: int = p.fit_omr(eoc=True, inserts=[False, True, True])
    assert p_result >= 0
