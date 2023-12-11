from my_project.auth.service import staff_service
from my_project.auth.controller.general_controller import GeneralController


class StaffController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = staff_service
