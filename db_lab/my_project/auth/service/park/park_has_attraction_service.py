from my_project.auth.dao import park_has_attraction_dao
from my_project.auth.service.general_service import GeneralService


class ParkHasAttractionService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = park_has_attraction_dao
