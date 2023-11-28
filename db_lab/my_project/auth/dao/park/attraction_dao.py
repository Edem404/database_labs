from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Attraction


class AttractionDAO(GeneralDAO):
    """
    Realisation of Attraction data access layer.
    """
    _domain_type = Attraction
