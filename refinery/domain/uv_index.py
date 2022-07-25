from dataclasses import dataclass

from refinery.lights.color import Color


@dataclass
class UVIndex:
    uv_index: float

    def is_low(self):
        return self.uv_index <= 3

    def get_color(self) -> Color:
        if self.uv_index < 2:
            # somewhat green
            return Color(hue=120, saturation=0.4, brightness=1, temperature=3500)
        elif self.uv_index < 8:
            # 2a + b = 120, when UVI = 2, color is green (120)
            # 8a + b = 0, when UVI = 8, color is red (0)
            a = -20
            b = 160
            hue = int(a * self.uv_index + b)
            return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
        else:
            # 8a + b = 360, when UVI = 8, color is red (360)
            # 11a + b = 300, when UVI = 11, color is violet (300)
            a = -20
            b = 360 + 160
            # not less than 300 (violet)
            hue = max(300, int(a * self.uv_index + b))
            return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
