from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Attraction(db.Model, IDto):
    __tablename__ = 'attraction'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    capacity = db.Column(db.Integer, nullable=False)
    parks = db.relationship('Park', secondary='park_has_attraction', back_populates='attractions')
    attraction_staff = db.relationship('AttractionStaff', back_populates='attraction')

    def __repr__(self) -> str:
        return f"<Attraction(id={self.id}, name={self.name}, capacity={self.capacity})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            # "region": self.region.put_into_dto() if self.region else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Attraction:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return Attraction(
                    name=dto_dict.get("name"),
                    capacity=dto_dict.get("capacity"),
                )
