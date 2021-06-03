from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models.pets import Pets


class RegisterPet(ABC):
    """Interface to RegisterPet use case"""

    @abstractclassmethod
    def registry(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Use case"""

        raise Exception("Should implement mehhod register.")
