from my_project.auth.dao import attraction_staff_dao
from my_project.auth.service.general_service import GeneralService


class AttractionStaffService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = attraction_staff_dao

    def find_attractions_by_staff_id(self, staff_id: int):
        return self._dao.find_attraction_by_staff_id(staff_id)
