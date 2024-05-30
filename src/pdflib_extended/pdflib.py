from core.pdflib_base import PDFlibBase
from extensions.barcodes import omr, code_128, datamatrix
from extensions.classes import Point, Box
from extensions.shapes import rectangle
from extensions.text import text_box


class PDFlib(PDFlibBase):
    def __init__(self, license_key: str = None):
        super().__init__()

        if license_key:
            self.set_option(f"license={license_key}")

    def fit_datamatrix(self, data: str, point: Point, scale: float = 0.35) -> int:
        return datamatrix(self, data, point, scale)

    def fit_code_128_barcode(self, data: str, box: Box, font_size: float = 24) -> int:
        return code_128(self, data, box, font_size)

    def fit_text_box(
        self,
        text: str,
        box: Box,
        font_name: str = "Arial",
        font_size: int = 12,
        tf_optlist: str = "",
        fit_optlist: str = "",
    ) -> int:
        return text_box(self, text, box, font_name, font_size, tf_optlist, fit_optlist)

    def fit_rectangle(
        self, box: Box, c: float = 0, m: float = 0, y: float = 0, k: float = 0
    ) -> int:
        return rectangle(self, box, c, m, y, k)

    def fit_omr(self, eoc: bool = False, inserts: list[bool] = None) -> int:
        return omr(self, eoc, inserts)


if __name__ == "__main__":
    p = PDFlib()
    print(isinstance(p, PDFlibBase))
