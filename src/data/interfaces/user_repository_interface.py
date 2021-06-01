from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """Abstract Method"""

        raise Exception("Method not implemented.")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """Abstract Method"""

        raise Exception("Method not implemented.")
