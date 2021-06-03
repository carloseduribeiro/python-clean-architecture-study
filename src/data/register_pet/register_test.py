from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet


faker = Faker()


def test_register():
    """Testing register method of RegisterPet"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "name": faker.name(),
        },
    }

    response = register_pet.registry(**attributes)

    # Testing inputs:
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]

    # Testinf FindUser inputs:
    assert find_user.by_id_and_name_params == attributes["user_information"]

    # Testinf outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing tegister method of RegisterPet in fail"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.random_number(digits=1),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "name": faker.name(),
        },
    }

    response = register_pet.registry(**attributes)

    # Testing inputs:
    assert pet_repo.insert_pet_params == {}

    # Testinf FindUser inputs:
    assert find_user.by_id_and_name_params == attributes["user_information"]

    # Testinf outputs:
    assert response["Success"] is False
    assert response["Data"] is None
