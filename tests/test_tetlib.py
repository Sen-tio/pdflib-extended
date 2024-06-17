from pdflib_extended.tetlib import TETLib


def test_tetlib_document_context(shared_datadir):
    t = TETLib()
    sample_file = shared_datadir / "sample.pdf"

    with t.open_document_ctx(sample_file) as doc:
        assert not doc.handle < 0
        assert doc.page_count > 0


def test_tetlib_page_context(shared_datadir):
    t = TETLib()
    sample_file = shared_datadir / "sample.pdf"

    with t.open_document_ctx(sample_file) as doc:
        with doc.open_page(1, optlist="granularity=page") as page:
            assert not page.handle < 0
            assert page.height != 0
            assert page.width != 0
            assert page.get_text() == "This is a Sample PDF file"
