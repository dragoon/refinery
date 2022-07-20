from abc import abstractmethod

from refinery.domain.device import AbstractDevice


class AbstractBulb(AbstractDevice):

    @abstractmethod
    def set_color(self) -> None:
        pass
