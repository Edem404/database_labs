from my_project.auth.dao import park_dao
from my_project.auth.service.general_service import GeneralService


class ParkService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = park_dao