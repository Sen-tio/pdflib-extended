from pdflib_extended.tetlib import TETLib


def test_tetlib(shared_datadir):
    t = TETLib(load_as_com_object=True)
    sample_file = shared_datadir / "sample.pdf"

    doc_handle = t.open_document(sample_file.as_posix(), "")
    if doc_handle < 0:
        print(t.get_errmsg())

    page_handle = t.open_page(doc_handle, 1, "granularity=page")
    if page_handle < 0:
        print(t.get_errmsg())

    text = t.get_text(page_handle)

    assert text == "This is a Sample PDF file"
