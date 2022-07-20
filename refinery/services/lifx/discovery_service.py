from functools import cache
from typing import List

from lifxlan import LifxLAN

from refinery.domain.lifx.bulb import LifxBulb


class LifxDiscoveryService:
    lan: LifxLAN
    lights: List[LifxBulb]

    def __init__(self):
        self.lan = LifxLAN()
        self.lights = [LifxBulb(l) for l in self.lan.get_lights()]

    @cache
    def find_bulbs_by_label(self, label: str) -> List[LifxBulb]:
        """
        Cached so we don't lookup light again and again
        :param label: label to lookup
        :return:
        """
        return [l for l in self.lights if l.get_label() == label]
