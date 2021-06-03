from typing import Type, Dict, List
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import FindPet as FindPetInterface
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """Class to define use case FindPet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet By id
        :param  - pet_id: id of the pet
        :return - Dicttionary with information of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet By user id
        :param  - user_id: id of the owner of the pet
        :return - Dicttionary with information of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet By id and User owner id
        :param  - pet_id: id of the pet
                - user_id: id of the owner of the pet
        :return - Dicttionary with information of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
