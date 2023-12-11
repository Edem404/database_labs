from typing import List

from my_project.auth.dao import client_dao
from my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = client_dao

    def insert_client(self, name, surname, age, phone):
        return self._dao.insert_client(name, surname, age, phone)

    def multi_insert(self):
        return self._dao.multi_insert()

    def age_statistics(self, stat_type: str) -> List[object]:
        return self._dao.age_statistics(stat_type)
