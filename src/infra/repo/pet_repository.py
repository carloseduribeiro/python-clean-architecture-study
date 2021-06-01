# pylint: disable=E1101

from src.domain.models.pets import Pets
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.pets import Pets as PetsModel


class PetRepository:
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Insert data in PetsEntity entity
        :param - name:      Name of the pet.
               - specie:    Enum with species acepted.
               - age:       Pet age.
               - user_id:   Id of the owner (FK)
        :return - Tuple with the new pet inserted.
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    new_pet.id,
                    new_pet.name,
                    new_pet.specie.value,
                    new_pet.age,
                    new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
