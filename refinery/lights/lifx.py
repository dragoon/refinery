from typing import Optional

from lifxlan import LifxLAN, Light


def get_light(label: str) -> Optional[Light]:
    lan = LifxLAN()
    lights = lan.get_lights()
    # need to call get_label as otherwise it's not initialized
    lights = [l for l in lights if l.get_label() and l.label == label]
    if len(lights) == 1:
        return lights[0]
    return None
