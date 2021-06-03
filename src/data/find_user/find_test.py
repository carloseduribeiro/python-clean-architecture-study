from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["user_id"])

    # Testing Inputs:
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method in fail"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.name()}

    response = find_user.by_id(user_id=attributes["user_id"])

    # Testing input:
    assert user_repo.select_user_params == {}

    # Testing output:
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """Testing by_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    # Testing Inputs:
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_name_fail():
    """Testing by_name method in fail"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.random_number(digits=2)}

    response = find_user.by_name(name=attributes["name"])

    # Testing input:
    assert user_repo.select_user_params == {}

    # Testing output:
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """Testing by_id_and_name"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # Testing Inputs:
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing Outputs:
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name_fail():
    """Testing by_id_and_name method in fail"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.name(), "name": faker.random_number(digits=2)}

    response = find_user.by_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # Testing input:
    assert user_repo.select_user_params == {}

    # Testing output:
    assert response["Success"] is False
    assert response["Data"] is None
