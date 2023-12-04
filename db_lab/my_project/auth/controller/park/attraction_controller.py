from my_project.auth.service import attraction_service
from my_project.auth.controller.general_controller import GeneralController


class AttractionController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = attraction_service

    def find_staff_in_attraction(self, attraction_id: int):
        return self._service.find_staff_in_attraction(attraction_id)

    def add_staff_to_attraction(self, attraction_id: int, staff_id: int):
        self._service.add_staff_to_attraction(attraction_id, staff_id)

    def delete_staff_from_attraction(self, attraction_id: int, staff_id: int):
        self._service.delete_staff_from_attraction(attraction_id, staff_id)
