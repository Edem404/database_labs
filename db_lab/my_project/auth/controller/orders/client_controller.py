from typing import List

from my_project.auth.service import client_service
from my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = client_service

    def insert_client(self, name, surname, age, phone):
        self._service.insert_client(name, surname, age, phone)

    def multi_insert(self):
        self._service.multi_insert()

    def age_statistics(self, stat_type: str) -> List[object]:
        return list(map(lambda x: dict(x), self._service.age_statistics(stat_type)))
