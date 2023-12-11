from my_project.auth.dao import order_dao
from my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    """
    Realisation of Client service.
    """

    # Realisation of dao of CLIENT not just general dao
    _dao = order_dao
