from typing import Optional

from lifxlan import LifxLAN, Light


def get_light(label: str) -> Optional[Light]:
    lan = LifxLAN()
    lights = lan.get_lights()
    lights = [l for l in lights if l.label == label]
    if len(lights) == 1:
        return lights[0]
    return None
