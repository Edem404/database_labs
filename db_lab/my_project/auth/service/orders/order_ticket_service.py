from my_project.auth.dao import order_ticket_dao
from my_project.auth.service.general_service import GeneralService


class OrderTicketService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = order_ticket_dao

    def delete_order_ticket(self, ticket_id: int, order_id: int) -> None:
        self._dao.delete_order_ticket(ticket_id, order_id)
