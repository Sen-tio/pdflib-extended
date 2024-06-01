from pdflib_extended.pdflib import PDFlib
from pdflib_extended.extensions.blocks import ImageBlock, TextBlock


def test_image_block(shared_datadir, tmp_path):
    p = PDFlib()
    tmp_file = tmp_path / "tmp.pdf"
    sample_file = shared_datadir / "sample.pdf"

    with p.start_document(tmp_file) as new_document, new_document.start_page(
        8.5 * 72, 11 * 72
    ) as _, p.open_document(sample_file) as document, document.open_page(1) as page:
        page.fit_page(0, 0)

        for block in page.blocks:
            if isinstance(block, TextBlock):
                block.fill_block(block.text)
            elif isinstance(block, ImageBlock):
                with p.read_image(shared_datadir / block.text) as image:
                    block.fill_block(image.handle)
