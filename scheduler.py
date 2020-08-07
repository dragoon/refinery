from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import timezone

from refinery.apis.weather import get_current_uv_index
from refinery.apis.weather.color_util import uvi_to_color
from refinery.lights.lifx import get_light

scheduler = BlockingScheduler()
UV_BULB = None


def get_uv_bulb():
    global UV_BULB
    if UV_BULB is None:
        UV_BULB = get_light(label="uv_index")
    return UV_BULB


@scheduler.scheduled_job(
    "cron", day_of_week="*", hour="*", minute="*", timezone=timezone("Europe/Zurich")
)
def uvi_scheduler():
    # 1. get current UV index
    uv_index = get_current_uv_index()
    # 2. set color according to the weather
    uv_color = uvi_to_color(uv_index)
    print("Setting UV color:", uv_color)
    uv_bulb = get_uv_bulb()
    if uv_bulb is not None:
        uv_bulb.set_color(uv_color.to_lifx_color())


scheduler.start()
