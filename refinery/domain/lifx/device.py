import functools
from lifxlan import Device, WorkflowException
from refinery.domain.device import AbstractDevice

import logging

logger = logging.getLogger(__name__)


def lifx_workflow(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except WorkflowException:
            logger.info(f"The device is inactive {self.device_id}")
    return wrapper


class LifxDevice(AbstractDevice):
    device: Device

    def __init__(self, device: Device):
        super().__init__(device.mac_addr)
        self.device = device

    @lifx_workflow
    def get_label(self):
        return self.device.get_label()

    @lifx_workflow
    def switch_on(self):
        self.device.set_power(True)

    @lifx_workflow
    def switch_off(self):
        self.device.set_power(False)



