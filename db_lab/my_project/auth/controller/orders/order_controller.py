from my_project.auth.service import order_service
from my_project.auth.controller.general_controller import GeneralController


class OrderController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = order_service
