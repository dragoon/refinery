from lifxlan import Light

from refinery.domain.bulb import AbstractBulb
from refinery.domain.lifx.device import LifxDevice, lifx_workflow
from refinery.lights.color import Color


class LifxBulb(LifxDevice, AbstractBulb):
    device: Light

    def __init__(self, device: Light):
        super().__init__(device)

    @lifx_workflow
    def set_color(self, color: Color):
        self.device.set_color(color.to_lifx_color())
