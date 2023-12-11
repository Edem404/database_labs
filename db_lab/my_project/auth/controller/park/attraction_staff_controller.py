from my_project.auth.service import attraction_staff_service
from my_project.auth.controller.general_controller import GeneralController


class AttractionStaffController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = attraction_staff_service

    def find_attractions_by_staff_id(self, staff_id: int):
        return self._service.find_attractions_by_staff_id(staff_id)