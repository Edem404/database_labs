from typing import List

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Region, City


class RegionDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Region

    def find_cities_by_index(self, index: int) -> List[City]:
        """
        Gets all shops in the city by city index.
        :param index: city index
        :return: list of shops
        """

        region = self._session.query(Region).filter(Region.name == index).first()

        if region:
            cities = self._session.query(City).filter(City.region_name == region.name).all()
            return [city.put_into_dto() for city in cities]
        return []

    def create_region_and_many_cities(self, region_name, cities_in_region: list):
        new_region = Region(name=region_name)
        self._session.add(new_region)

        for city_name in cities_in_region:
            new_city = City(name=city_name, region_name=region_name)
            self._session.add(new_city)

        self._session.commit()

    def create_db(self):
        self._session.execute(sqlalchemy.text("CALL create_databases_and_tables()"))
        self._session.commit()
