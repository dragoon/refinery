import logging

from dotenv import load_dotenv
from refinery.logging_config import setup_logging
from refinery.services.lifx.discovery_service import LifxDiscoveryService

load_dotenv(verbose=True)
from refinery.apis.uvi import get_current_uv_index

service = LifxDiscoveryService()

LABEL = "uv_index"


def update_lights():
    uv_bulbs = service.find_bulbs_by_label(LABEL)
    logger = logging.getLogger(__name__)
    for uv_bulb in uv_bulbs:
        logger.info(f"Bulb with label '{LABEL}' is found with IP address: {uv_bulb.device.get_ip_addr()}")
        # 1. get current UV index
        uv_index = get_current_uv_index()
        logger.info(f"Current UV index: {uv_index}")
        # 2. set color according to the UV index
        uv_color = uv_index.get_color()
        logger.info(f"Setting UV color: {uv_color}")
        uv_bulb.set_color(uv_color)
        if uv_index.is_low():
            uv_bulb.switch_off()
        else:
            uv_bulb.switch_on()
    else:
        logger.info(f"Found {len(uv_bulbs)} UV bulbs")


if __name__ == "__main__":
    setup_logging("refinery")
    update_lights()
