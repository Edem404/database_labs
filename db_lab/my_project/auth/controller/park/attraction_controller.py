from my_project.auth.service import attraction_service
from my_project.auth.controller.general_controller import GeneralController


class AttractionController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = attraction_service
