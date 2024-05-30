from contextlib import AbstractContextManager
from typing import Union, Optional, Self

from pdflib_extended.core.pdflib_base import PDFlibBase
from pdflib_extended.exceptions import InvalidDocumentHandle, InvalidPageHandle


class Page(AbstractContextManager):
    def __init__(
        self,
        p: PDFlibBase,
        document_handle: int,
        page_number: int,
        optlist: Optional[str] = "",
    ) -> None:
        self.p = p
        self.document_handle = document_handle
        self.page_number = page_number
        self.optlist = optlist

    def __enter__(self) -> Self:
        self.handle: int = self.p.open_pdi_page(
            self.document_handle, self.page_number, self.optlist
        )
        if self.handle < 0:
            raise InvalidPageHandle(self.p.get_errmsg())

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.p.close_pdi_page(self.handle)


class Document(AbstractContextManager):
    def __init__(
        self, p: PDFlibBase, file_path: Union[str, Path], optlist: str = ""
    ) -> None:
        self.p = p
        self.file_path = Path(file_path)
        self.optlist = optlist

    def __enter__(self) -> Self:
        self.handle: int = self.p.open_pdi_document(
            self.file_path.as_posix(), self.optlist
        )
        if self.handle < 0:
            raise InvalidDocumentHandle(self.p.get_errmsg())

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.p.close_pdi_document(self.handle)

    def open_page(self, page_number: int, optlist: Optional[str] = "") -> Page:
        return Page(self.p, self.handle, page_number, optlist)
