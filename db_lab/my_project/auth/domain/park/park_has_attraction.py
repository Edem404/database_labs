from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkHasAttraction(db.Model, IDto):
    __tablename__ = 'park_has_attraction'

    park_id = db.Column(db.Integer, db.ForeignKey('park.id'), primary_key=True)
    attraction_id = db.Column(db.Integer, db.ForeignKey('attraction.id'), primary_key=True)
    number = db.Column(db.Integer)

    parks = db.relationship('Park', backref='parks_has_attractions')
    attractions = db.relationship('Attraction', backref='parks_has_attractions')
    def __repr__(self) -> str:
        return f"<Park has Attraction(park_id={self.park_id}, attraction_id={self.attraction_id}, number={self.number})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "park_id": self.park_id,
            "attraction_id": self.attraction_id,
            "number": self.number,
            # "region": self.region.put_into_dto() if self.region else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkHasAttraction:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return ParkHasAttraction(
                    park_id=dto_dict.get("park_id"),
                    attraction_id=dto_dict.get("attraction_id"),
                    number=dto_dict.get("number")
                )
