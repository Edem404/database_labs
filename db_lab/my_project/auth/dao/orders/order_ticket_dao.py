from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import OrderTicket


class OrderTicketDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = OrderTicket

    def delete_order_ticket(self, ticket_id: int, order_id: int) -> None:
        # order_ticket = OrderTicket.query.filter_by(ticket_id=ticket_id, order_id=order_id).first()
        order_ticket = self._session.query(self._domain_type).get((ticket_id, order_id))
        if order_ticket:
            self._session.delete(order_ticket)
            self._session.commit()
