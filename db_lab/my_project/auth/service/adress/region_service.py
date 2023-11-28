from my_project.auth.dao import region_dao
from my_project.auth.service.general_service import GeneralService


class RegionService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = region_dao

    def find_cities_by_index(self, region_id: str):
        return self._dao.find_cities_by_index(region_id)