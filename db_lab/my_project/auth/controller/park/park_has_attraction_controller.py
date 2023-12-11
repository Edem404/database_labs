from my_project.auth.service import park_has_attraction_service
from my_project.auth.controller.general_controller import GeneralController


class ParkHasAttractionController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = park_has_attraction_service
