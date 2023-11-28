from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Park(db.Model, IDto):
    __tablename__ = 'park'

    id = db.Column(db.Integer, primary_key=True)
    max_visitors_per_day = db.Column(db.Integer, nullable=True)
    open_time = db.Column(db.String(11), nullable=False)
    city_name = db.Column(db.String(45), db.ForeignKey('city.name'), nullable=False)
    staff = db.relationship('Staff', backref='park', lazy=True)
    ticket = db.relationship('Ticket', backref='park', lazy=True)
    attractions = db.relationship('Attraction', secondary='park_has_attraction', back_populates='parks')


    def __repr__(self) -> str:
        return f"<Park(id={self.id}, max_visitors_per_day={self.max_visitors_per_day}, open_time={self.open_time}, city_name={self.city_name})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "max_visitors_per_day": self.max_visitors_per_day,
            "open_time": self.open_time,
            "city_name": self.city_name,
            # "region": self.region.put_into_dto() if self.region else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Park:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return Park(
                    max_visitors_per_day=dto_dict.get("max_visitors_per_day"),
                    open_time=dto_dict.get("open_time"),
                    city_name=dto_dict.get("city_name"),
                )