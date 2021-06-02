from faker import Faker
from src.domain.models.users import Users

faker = Faker()


def mock_user() -> Users:
    """Mock Users"""
    return Users(
        id=faker.random_number(digits=5), name=faker.name(), password=faker.name()
    )
