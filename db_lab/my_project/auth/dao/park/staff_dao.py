from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Staff


class StaffDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Staff
