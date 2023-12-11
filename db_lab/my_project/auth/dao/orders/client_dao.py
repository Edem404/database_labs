from typing import List

import sqlalchemy
from sqlalchemy import text
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_number(self, surname: str) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param surname: surname value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.surname == surname).order_by(Client.surname).all()

    def insert_client(self, name: str, surname: str, age: int, phone: str):
        self._session.execute(sqlalchemy.text("CALL insert_client(:p1, :p2, :p3, :p4)"),
            {"p1": name, "p2": surname, "p3": age, "p4": phone})

        self._session.commit()

    def multi_insert(self):
        self._session.execute(sqlalchemy.text("CALL multi_insert()"))
        self._session.commit()

    def age_statistics(self, stat_type: str) -> List[object]:
        return self._session.execute(sqlalchemy.text("CALL call_client_age_statistics(:stat_type)"),
                                     {"stat_type": stat_type}).mappings().all()
