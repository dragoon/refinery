from dataclasses import dataclass
from typing import Tuple


@dataclass
class Color:
    """
    color is [Hue, Saturation, Brightness, Temperature (in Kelvin)]
    """

    hue: int
    saturation: int
    brightness: int
    temperature: int

    def to_lifx_color(self) -> Tuple[int, int, int, int]:
        return self.hue, self.saturation, self.brightness, self.temperature
