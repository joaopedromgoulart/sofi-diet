from abc import ABC, abstractmethod


class BodyFat(ABC):
    @abstractmethod
    def calculate(self):
        'calculate the bodyfat'
