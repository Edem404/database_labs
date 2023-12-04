from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


attraction_has_staff = db.Table(
    'attraction_has_staff',
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.id'), primary_key=True),
    db.Column('attraction_id', db.Integer, db.ForeignKey('attraction.id'), primary_key=True),
    db.UniqueConstraint('staff_id', 'attraction_id', name='uq_attraction_has_staff1'),
    extend_existing=True
)


class Staff(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "staff"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    surname = db.Column(db.String(45))
    phonenumber = db.Column(db.String(13), unique=True, nullable=True)
    park_id = db.Column(db.Integer, db.ForeignKey('park.id'), nullable=False)
    attraction_staff = db.relationship('AttractionStaff', back_populates='staff')

    attractions = db.relationship("Attraction", secondary="attraction_has_staff", back_populates="staff")

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Staff({self.id}, '{self.name}', '{self.surname}', '{self.phonenumber}', '{self.park_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phonenumber": self.phonenumber,
            "park_id": self.park_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Staff:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Staff(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phonenumber=dto_dict.get("phonenumber"),
            park_id=dto_dict.get("park_id"),
            # client_type_id=dto_dict.get("client_type_id")
        )
        return obj
