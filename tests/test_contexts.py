import pytest
from pdflib_extended.pdflib import PDFlib
from pathlib import Path

from pdflib_extended.utils.contexts import Document, Page


@pytest.fixture(scope="function")
def begin_document_scoped_pdflib_object(tmp_path) -> PDFlib:
    tmp_file = tmp_path / "tmp.pdf"
    p = PDFlib()
    p.begin_document(tmp_file.as_posix(), "")
    yield p


def test_document_context(begin_document_scoped_pdflib_object, shared_datadir):
    p: PDFlib = begin_document_scoped_pdflib_object
    document_path: Path = shared_datadir / "sample.pdf"

    with Document(p, document_path) as document:
        assert document.handle >= 0


def test_page_context(begin_document_scoped_pdflib_object, shared_datadir):
    p: PDFlib = begin_document_scoped_pdflib_object
    document_path: Path = shared_datadir / "sample.pdf"

    with Document(p, document_path) as document:
        with document.open_page(page_number=1) as page:
            assert page.handle >= 0
