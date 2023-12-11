from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Park


class ParkDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Park
