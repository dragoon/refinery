from apscheduler.schedulers.blocking import BlockingScheduler

from dotenv import load_dotenv
from lifxlan import WorkflowException

load_dotenv(verbose=True)

from refinery.logging_util import setup_logging
from refinery.apis.uvi import get_current_uv_index
from refinery.apis.uvi.color_util import uvi_to_color
from refinery.lights.lifx import get_light

scheduler = BlockingScheduler()
logger = setup_logging()
UV_BULB = None


def get_uv_bulb():
    global UV_BULB
    if UV_BULB is None:
        UV_BULB = get_light(label="uv_index")
    return UV_BULB


@scheduler.scheduled_job("interval", minutes=10)
def uvi_scheduler():
    uv_bulb = get_uv_bulb()
    if uv_bulb is not None:
        logger.info(f"Bulb with label {uv_bulb.label} is found with IP address: {uv_bulb.get_ip_addr()}")
        # 1. get current UV index
        uv_index = get_current_uv_index()
        logger.debug(f"Current UV index: {uv_index}")
        # 2. set color according to the weather
        uv_color = uvi_to_color(uv_index)
        logger.debug(f"Setting UV color: {uv_color}")
        try:
            uv_bulb.set_color(uv_color.to_lifx_color())
        except WorkflowException:
            logger.info(f"The bulb is inactive {uv_bulb.label}")
            global UV_BULB
            UV_BULB = None


scheduler.start()
