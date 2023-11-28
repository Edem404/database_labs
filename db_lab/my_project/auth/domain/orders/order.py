from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Order(db.Model, IDto):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    total_price = db.Column(db.String(45), nullable=True)

    client = db.relationship('Client', back_populates='orders')

    def __repr__(self):
        return f"<Order(id={self.id}, client_id={self.client_id}, date={self.date}, total_price={self.total_price})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "date": self.date,
            "total_price": self.total_price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Order(
            client_id=dto_dict.get("client_id"),
            date=dto_dict.get("date"),
            total_price=dto_dict.get("total_price"),
        )
        return obj
