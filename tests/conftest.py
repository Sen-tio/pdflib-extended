import pytest
from pdflib_extended.pdflib import PDFlib


@pytest.fixture(scope="function")
def new_page_scoped_pdflib_object(tmp_path) -> PDFlib:
    p = PDFlib()
    tmp_file = tmp_path / "tmp.pdf"

    with p.start_document(tmp_file) as new_document:
        with new_document.start_page(8.5 * 72, 11 * 72) as _:
            yield p
