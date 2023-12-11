from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Ticket(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    in_stock = db.Column(db.Integer, nullable=True)
    date = db.Column(db.String(10), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    special_ticket = db.Column(db.Integer, nullable=True)
    park_id = db.Column(db.Integer, db.ForeignKey('park.id'), nullable=False)

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Ticket({self.id}, '{self.in_stock}', '{self.date}', '{self.price}', '{self.special_ticket}', '{self.park_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "in_stock": self.in_stock,
            "date": self.date,
            "price": self.price,
            "special_ticket": self.special_ticket,
            "park_id": self.park_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ticket:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Ticket(
            in_stock=dto_dict.get("in_stock"),
            date=dto_dict.get("date"),
            price=dto_dict.get("price"),
            special_ticket=dto_dict.get("special_ticket"),
            park_id=dto_dict.get("park_id"),
            # client_type_id=dto_dict.get("client_type_id")
        )
        return obj
