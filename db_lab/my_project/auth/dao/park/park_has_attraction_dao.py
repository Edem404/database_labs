from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ParkHasAttraction


class ParkHasAttractionDAO(GeneralDAO):
    """
    Realisation of Attraction data access layer.
    """
    _domain_type = ParkHasAttraction
