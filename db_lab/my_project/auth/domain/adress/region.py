from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Region(db.Model, IDto):
    __tablename__ = "region"

    name = db.Column(db.String(45), primary_key=True)
    cities = db.relationship('City', backref='region', lazy=True)
    
    def __repr__(self) -> str:
        return f"<Region(name={self.name})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Region:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Region(name=dto_dict.get("name"))
        return obj
