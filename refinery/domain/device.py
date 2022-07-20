from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    device_id: str

    def __init__(self, device_id: str):
        self.device_id = device_id

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AbstractDevice):
            return False
        return self.device_id == o.device_id

    @abstractmethod
    def get_label(self) -> str:
        pass

    @abstractmethod
    def switch_on(self) -> None:
        pass

    @abstractmethod
    def switch_off(self) -> None:
        pass



