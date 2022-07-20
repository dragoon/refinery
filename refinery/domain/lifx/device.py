from lifxlan import Device

from refinery.domain.device import AbstractDevice


class LifxDevice(AbstractDevice):
    device: Device

    def __init__(self, device: Device):
        super().__init__(device.mac_addr)
        self.device = device

    def get_label(self):
        return self.device.get_label()

    def switch_on(self):
        self.device.set_power(True)

    def switch_off(self):
        self.device.set_power(False)



