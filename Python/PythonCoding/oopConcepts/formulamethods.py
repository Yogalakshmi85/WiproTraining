from abc import  ABC, abstractmethod #Abstract Base class Modules

class FormulaMethods(ABC):
    # @abstractmethod
    def calculate_area(self):
        pass

    # @abstractmethod #decorator
    def calculate_perimeter(self):
        pass