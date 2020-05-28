import abc
from typing import Optional

from decker.conf import Config


class Formatter(abc.ABC):
    id: str = NotImplemented

    version: Optional[str] = None

    @property
    def display(self):
        if self.version:
            return f'{self.id}=={self.version}'
        return self.id

    @abc.abstractmethod
    def run(self, config: Config) -> None:
        ...
