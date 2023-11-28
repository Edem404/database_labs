from typing import List

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
        # Отримати місто за індексом
        region = self._session.query(Region).filter(Region.name == index).first()

        if region:
            # Отримати всі магазини, які мають city_id, яке відповідає індексу міста
            cities = self._session.query(City).filter(City.region_name == region.name).all()
            return [city.put_into_dto() for city in cities]
        return []