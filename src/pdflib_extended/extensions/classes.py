from dataclasses import dataclass
from typing import Self


@dataclass
class Box:
    llx: float
    lly: float
    urx: float
    ury: float

    def as_pt(self) -> Self:
        return Box(self.llx * 72, self.lly * 72, self.urx * 72, self.ury * 72)


@dataclass
class Point:
    x: float
    y: float

    def as_pt(self) -> Self:
        return Point(self.x * 72, self.y * 72)
