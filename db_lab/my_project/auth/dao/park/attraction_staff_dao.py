from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import AttractionStaff, Attraction


class AttractionStaffDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = AttractionStaff

    def find_attraction_by_staff_id(self, staff_id: int) -> List[Attraction]:
        """
        Gets all cars associated with a specific order.
        :param staff_id: Staff ID
        :return: list of attractions
        """
        attractions_staff = self._session.query(AttractionStaff).filter(AttractionStaff.staff_id == staff_id).all()
        if attractions_staff:
            all_attr_id = [attraction_staff.attraction_id for attraction_staff in attractions_staff]
            attractions = self._session.query(Attraction).filter(Attraction.id.in_(all_attr_id)).all()
            return [attraction.put_into_dto() for attraction in attractions]
        return []
