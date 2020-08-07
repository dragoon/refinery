from refinery.lights.color import Color


def uvi_to_color(uv_index: float) -> Color:
    if uv_index < 3:
        # somewhat green
        return Color(hue=16173, saturation=65535, brightness=65535, temperature=3500)
    elif uv_index < 6:
        # somewhat yellow
        return Color(hue=9000, saturation=65535, brightness=65535, temperature=3500)
    elif uv_index < 8:
        # somewhat orange
        return Color(hue=6500, saturation=65535, brightness=65535, temperature=3500)
    elif uv_index < 11:
        # somewhat red
        return Color(hue=65535, saturation=65535, brightness=65535, temperature=3500)
    else:
        # somewhat violet
        return Color(hue=50486, saturation=65535, brightness=65535, temperature=3500)
