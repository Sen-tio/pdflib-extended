import sys
from typing import Optional

from .core.tetlib_base import TETLibBase


class TETLib(TETLibBase):
    def __new__(cls, *args, **kwargs):
        if kwargs.get("load_as_com_object", False):
            if sys.platform != "win32":
                raise RuntimeError("COM objects can only be loaded on Windows")

            from .core.tetlib_base import TETLibCOMBase

            DynamicClass = type("DynamicClass", (TETLibCOMBase,), {})
            instance = super(TETLib, cls).__new__(DynamicClass)
            DynamicClass.__init__(instance)
            return instance

        return super().__new__(cls)

    def __init__(
        self, license_key: Optional[str] = None, load_as_com_object: bool = False
    ) -> None:
        super().__init__()

        if license_key:
            self.set_option(f"license={license_key}")
