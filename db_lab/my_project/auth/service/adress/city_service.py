from my_project.auth.dao import city_dao
from my_project.auth.service.general_service import GeneralService


class CityService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = city_dao
