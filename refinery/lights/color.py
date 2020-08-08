from dataclasses import dataclass
from typing import Tuple


@dataclass
class Color:
    """
    color is [Hue (0-360), Saturation (0-1), Brightness (0-1), Temperature (in Kelvin)]
    """

    hue: int
    saturation: float
    brightness: float
    temperature: int

    def to_lifx_color(self) -> Tuple[int, int, int, int]:
        return int(self.hue*65535/360), int(self.saturation*65535), int(self.brightness*65535), self.temperature
