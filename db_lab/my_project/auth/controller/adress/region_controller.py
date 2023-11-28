from my_project.auth.service import region_service
from my_project.auth.controller.general_controller import GeneralController


class RegionController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = region_service

    def find_cities_by_index(self, region_id: str):
        return self._service.find_cities_by_index(region_id)
