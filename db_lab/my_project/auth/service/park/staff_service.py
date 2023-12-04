from my_project.auth.dao import staff_dao
from my_project.auth.service.general_service import GeneralService


class StaffService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = staff_dao