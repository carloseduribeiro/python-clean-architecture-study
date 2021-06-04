from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController

faker = Faker()


def test_handle():
    """Testing Handle Method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(digits=5), "user_name": faker.word()}
    )

    response = find_user_controller.handle(http_request)

    # Testing inputs:
    assert (
        find_user_use_case.by_id_and_name_params["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_params["name"]
        == http_request.query["user_name"]
    )

    # Testing outputs:
    assert response.status_code == 200
    assert response.body


def test_handle_by_id():
    """Testinf Handle method with by_id query"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number(digits=5)})

    response = find_user_controller.handle(http_request)

    # Testing input:
    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]

    # Testing output:
    assert response.status_code == 200
    assert response.body


def test_handle_by_name():
    """Testinf Handle method with by_name query"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_name": faker.name()})

    response = find_user_controller.handle(http_request)

    # Testing input:
    assert find_user_use_case.by_name_param["name"] == http_request.query["user_name"]

    # Testing output:
    assert response.status_code == 200
    assert response.body


def test_handle_no_query_params():
    """Testing Handle Method with no query params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    # Testing inputs:
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing outputs:
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_invalid_query():
    """Testing Handle Method with invalid query params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"any": faker.word()})

    response = find_user_controller.handle(http_request)

    # Testing inputs:
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing outputs:
    assert response.status_code == 422
    assert "error" in response.body
