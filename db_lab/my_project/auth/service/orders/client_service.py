from my_project.auth.dao import client_dao
from my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = client_dao
