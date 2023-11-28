from my_project.auth.dao import attraction_dao
from my_project.auth.service.general_service import GeneralService


class AttractionService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = attraction_dao
