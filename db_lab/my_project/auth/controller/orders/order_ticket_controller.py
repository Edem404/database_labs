from my_project.auth.service import order_ticket_service
from my_project.auth.controller.general_controller import GeneralController


class OrderTicketController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = order_ticket_service

    def delete_order_ticket(self, ticket_id: int, order_id: int) -> None:
        self._service.delete_order_ticket(ticket_id, order_id)
