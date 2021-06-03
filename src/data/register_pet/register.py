from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.domain.use_cases import RegisterPet as RegistryPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets, Users


class RegisterPet(RegistryPetInterface):
    """Class to define use case: RegisterPet"""

    def __init__(
        self, pet_repository: Type[PetRepository], find_user: Type[FindUser]
    ) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Pet
        :param  - name:             pet name.
                - specie:           type of the specie.
                - age:              age of the pet.
                - user_information: Dictionary with user_id and/or user name.
        :return - Dicitionary with information of the process.
        """

        response = None

        # Validates entry and trying to find a user:
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name, specie, age, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Checks the user information and select the user
        :param  - user_information: Dictionary with user_id and/or user name.
        :return - Dictionary with the resonse of the FindUser use case.
        """

        user_founded = None
        user_params = set(user_information.keys())

        if "user_id" in user_params and "name" in user_params:
            user_founded = self.find_user.by_id_and_name(**user_information)

        elif "user_id" not in user_params and "name" in user_params:
            user_founded = self.find_user.by_name(**user_information)

        elif "user_id" in user_params and "name" not in user_params:
            user_founded = self.find_user.by_id(**user_information)

        else:
            return {"Success": False, "Data": None}

        return user_founded
