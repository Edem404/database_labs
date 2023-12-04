from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Order


class OrderDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Order

    def find_by_date(self, date: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.date == date).order_by(Order.date).all()