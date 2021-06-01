# pylint: disable=E1101

from typing import List
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

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Select data in pet entity by id and/or user id.
        :param  - pet_id:    Id of the pet registry.
                - user_id:   Id of the owner.
        :return - List with the pets selected.
        """

        try:
            query_data = None

            if pet_id and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                query_data = [data]

            elif user_id and not pet_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif pet_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
