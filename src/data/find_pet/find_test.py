from faker import Faker
from .find import FindPet
from src.infra.test import PetRepositorySpy

faker = Faker()


def test_by_pet_id():
    """Testing by_pet_id method in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing Inputs:
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_fail():
    """Testing by_pet_id method in fail"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.name()}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing input:
    assert pet_repo.select_pet_params == {}

    # Testing output:
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """Testing test_by_id_user method"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # Testing Inputs:
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_user_fail():
    """Testing test_by_id_user method in fail"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.name()}

    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # Testing input:
    assert pet_repo.select_pet_params == {}

    # Testing output:
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_pet_id_and_user_id():
    """Testing test_by_pet_id_and_user_id"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # Testing Inputs:
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id_fail():
    """Testing test_by_pet_id_and_user_id method in fail"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    response = find_pet.by_pet_id_and_user_id(pet_id=faker.name(), user_id=faker.name())

    # Testing Inputs:
    assert pet_repo.select_pet_params == {}

    # Testing Outputs:
    assert response["Success"] is False
    assert response["Data"] is None
