from typing import Dict, List
from src.domain.models import Users
from src.domain.test import mock_user


class FindUserSpy:
    """Class to define user case: Select User"""

    def __init__(self, user_repository: any) -> None:
        self.user_repository = user_repository
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_params = {}

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by id"""

        response = None
        self.by_id_param["user_id"] = user_id
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_user()]

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: int) -> Dict[bool, List[Users]]:
        """Select User By name"""

        response = None
        self.by_name_param["name"] = name
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_user()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select User By id and name"""

        response = None
        self.by_id_and_name_params["user_id"] = user_id
        self.by_id_and_name_params["name"] = name
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_user()]

        return {"Success": validate_entry, "Data": response}
