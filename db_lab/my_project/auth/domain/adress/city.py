from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    __tablename__ = "city"

    name = db.Column(db.String(45), primary_key=True)
    region_name = db.Column(db.String(45), db.ForeignKey('region.name'), nullable=False)
    parks = db.relationship('Park', backref='city', lazy=True)
    # address = db.relationship('Adress', backref='city', lazy=True)

    def __repr__(self) -> str:
        return f"<City(name={self.name}, region_name={self.region_name})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "name": self.name,
            "region_name": self.region_name,
            "region": self.region.put_into_dto() if self.region else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return City(name=dto_dict.get("name"), region_name=dto_dict.get("region_name"))