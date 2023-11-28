from my_project.auth.dao import ticket_dao
from my_project.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = ticket_dao
