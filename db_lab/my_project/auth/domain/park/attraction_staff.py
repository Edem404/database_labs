from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class AttractionStaff(db.Model, IDto):
    __tablename__ = 'attraction_staff'

    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True)
    attraction_id = db.Column(db.Integer, db.ForeignKey('attraction.id'), primary_key=True)

    staff = db.relationship('Staff', back_populates='attraction_staff')
    attraction = db.relationship('Attraction', back_populates='attraction_staff')

    def __repr__(self) -> str:
        return f"<Staff in attraction(staff_id={self.staff_id}, attraction_id={self.attraction_id})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "staff_id": self.staff_id,
            "attraction_id": self.attraction_id,
            # "region": self.region.put_into_dto() if self.region else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AttractionStaff:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return AttractionStaff(
                    staff_id=dto_dict.get("staff_id"),
                    attraction_id=dto_dict.get("attraction_id"),
                )
