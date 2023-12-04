from my_project.auth.dao import attraction_dao
from my_project.auth.service.general_service import GeneralService


class AttractionService(GeneralService):

    _dao = attraction_dao

    def find_staff_in_attraction(self, attraction_id: int):
        return self._dao.find_staff_in_attraction(attraction_id)

    def add_staff_to_attraction(self, attraction_id: int, staff_id: int):
        self._dao.add_staff_to_attraction(attraction_id, staff_id)

    def delete_staff_from_attraction(self, attraction_id: int, staff_id: int):
        self._dao.delete_staff_from_attraction(attraction_id, staff_id)
