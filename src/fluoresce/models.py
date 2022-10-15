from dataclasses import dataclass
from typing import Optional, List, Dict
from rich.style import Style
from re import Pattern

color_types = ["highlight", "link"]


class SimpleColor:
    style: Style


@dataclass(frozen=True)
class Color(SimpleColor):
    components: Dict[str, SimpleColor]


@dataclass(frozen=True)
class RegexColor(Color):
    regex: Pattern


@dataclass(frozen=True)
class ColorRef:
    palette_color_index: int
    palette_id: str


@dataclass(frozen=True)
class Palette:
    colors: List[Color]
