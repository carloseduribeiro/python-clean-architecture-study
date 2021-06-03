from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FundPet use case"""

    @abstractclassmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement method: by_ped_id")

    @abstractclassmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement method: by_user_id")

    @abstractclassmethod
    def by_pet_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement  method: by_pet_id_and_user_id")
