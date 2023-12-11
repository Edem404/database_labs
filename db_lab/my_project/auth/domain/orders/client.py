from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Client(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    surname = db.Column(db.String(45))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(13))
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.name}', '{self.surname}', '{self.age}', '{self.phone}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "phone": self.phone,
            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Client(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            age=dto_dict.get("age"),
            phone=dto_dict.get("phone")
            # client_type_id=dto_dict.get("client_type_id")
        )
        return obj
