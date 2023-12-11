from my_project.auth.service import park_service
from my_project.auth.controller.general_controller import GeneralController


class ParkController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = park_service
