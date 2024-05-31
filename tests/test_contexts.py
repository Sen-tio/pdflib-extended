import pytest
from pdflib_extended.pdflib import PDFlib
from pathlib import Path

from pdflib_extended.exceptions import EmptyNewDocumentException
from pdflib_extended.utils.contexts import Document, NewDocument, Image, NewPage


@pytest.fixture(scope="function")
def new_document_scoped_pdflib_object(tmp_path) -> PDFlib:
    p = PDFlib()
    tmp_file = tmp_path / "tmp.pdf"

    with p.start_document(tmp_file) as new_document:
        yield p

        # If the test function did not add any pages add one to avoid exception
        if new_document.page_count == 0:
            with new_document.start_page(1, 1):
                pass


def test_document_context(new_document_scoped_pdflib_object, shared_datadir):
    p: PDFlib = new_document_scoped_pdflib_object
    document_path: Path = shared_datadir / "sample.pdf"

    with p.open_document(document_path) as document:
        assert document.handle >= 0
        assert document.page_count == 1


def test_page_context(new_document_scoped_pdflib_object, shared_datadir):
    p: PDFlib = new_document_scoped_pdflib_object
    document_path: Path = shared_datadir / "sample.pdf"

    with p.open_document(document_path) as document:
        with NewPage(p, 8.5 * 72, 11 * 72) as new_page:
            with document.open_page(page_number=1) as page:
                page.fit_page(0, 0)
                assert page.handle >= 0
                assert page.width == 8.5 * 72
                assert page.height == 11 * 72


def test_new_document_context(tmp_path):
    p = PDFlib()
    tmp_file = tmp_path / "tmp.pdf"

    with pytest.raises(EmptyNewDocumentException):
        with NewDocument(p, tmp_file) as new_document:
            pass


def test_new_page_context(tmp_path):
    p = PDFlib()
    tmp_file = tmp_path / "tmp.pdf"

    with NewDocument(p, tmp_file) as new_document:
        with new_document.start_page(8.5 * 72, 11 * 72) as new_page:
            pass


def test_image_context(new_document_scoped_pdflib_object, shared_datadir):
    p = new_document_scoped_pdflib_object
    image_path = shared_datadir / "sample.png"

    with NewPage(p, 8.5 * 72, 11 * 72) as new_page:
        with Image(p, image_path) as image:
            image.fit_image(0, 0)
            assert image.handle >= 0
            assert image.width > 0
            assert image.height > 0
