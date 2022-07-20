from lifxlan import Light

from refinery.domain.lifx.device import LifxDevice
from refinery.lights.color import Color


class LifxBulb(LifxDevice):
    device: Light

    def __init__(self, device: Light):
        super().__init__(device)

    def set_color(self, color: Color):
        self.device.set_color(color.to_lifx_color())
