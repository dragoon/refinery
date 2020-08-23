from refinery.lights.color import Color


def uvi_to_color(uv_index: float) -> Color:
    if uv_index < 3:
        # somewhat green
        return Color(hue=111, saturation=1, brightness=1, temperature=3500)
    elif uv_index < 6:
        # somewhat yellow
        a = (63 - 111) / 3
        b = 2 * 111 - 63
        hue = int(a * uv_index + b)
        return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
    elif uv_index < 8:
        # somewhat orange
        a = (46 - 63) / 2
        b = (8 * 63 - 6 * 46) / 2
        hue = int(a * uv_index + b)
        return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
    elif uv_index < 11:
        # somewhat red
        a = (8 - 46) / 3
        b = (11 * 46 - 8 * 8) / 3
        hue = int(a * uv_index + b)
        return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
    else:
        # somewhat violet
        a = (294 - 360) / 2
        b = (13 * 360 - 11 * 294) / 2
        hue = int(a * uv_index + b)
        return Color(hue=hue, saturation=1, brightness=1, temperature=3500)
