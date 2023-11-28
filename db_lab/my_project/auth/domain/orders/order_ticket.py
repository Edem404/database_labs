from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class OrderTicket(db.Model, IDto):
    __tablename__ = 'order_ticket'

    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    number_of_tickets = db.Column(db.Integer, nullable=True)

    ticket = db.relationship('Ticket', backref='order_tickets')
    order = db.relationship('Order', backref='order_tickets')
    # ticket = db.relationship('Ticket', back_populates='order_tickets')
    # order = db.relationship('Order', back_populates='order_tickets')

    def __repr__(self):
        return f"<OrderTicket(ticket_id={self.ticket_id}, " \
               f"order_id={self.order_id}, number_of_tickets={self.number_of_tickets})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ticket_id": self.ticket_id,
            "order_id": self.order_id,
            "number_of_tickets": self.number_of_tickets,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrderTicket:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = OrderTicket(
            ticket_id=dto_dict.get("ticket_id"),
            order_id=dto_dict.get("order_id"),
            number_of_tickets=dto_dict.get("number_of_tickets"),
            # client_type_id=dto_dict.get("client_type_id")
        )
        return obj
