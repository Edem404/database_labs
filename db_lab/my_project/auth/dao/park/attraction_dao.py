from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Attraction
from my_project.auth.domain import Staff
from my_project.auth.domain import attraction_has_staff


class AttractionDAO(GeneralDAO):
    """
    Realisation of Attraction data access layer.
    """
    _domain_type = Attraction

    def find_staff_in_attraction(self, attraction_id: int):

        attraction = self._session.query(Attraction).filter_by(id=attraction_id).first()

        staff_ids = (
            self._session.query(attraction_has_staff.c.staff_id)
            .filter(attraction_has_staff.c.attraction_id == attraction_id)
            .all()
        )

        staff_id = [staff_id for (staff_id, ) in staff_ids]

        print("Staff IDs:", staff_id)
        staffs = self._session.query(Staff).filter(Staff.id.in_(staff_id)).all()
        print("Number of staffs:", len(staffs))

        attraction_data = {
            "attraction": attraction.put_into_dto(),
            "staff": [staff.put_into_dto() for staff in staffs]
        }

        return attraction_data

    def add_staff_to_attraction(self, attraction_id: int, staff_id: int):

        self._session.execute(attraction_has_staff.insert().values(attraction_id=attraction_id, staff_id=staff_id))

        self._session.commit()

    def delete_staff_from_attraction(self, attraction_id: int, staff_id: int) -> None:
        self._session.execute(
            attraction_has_staff.delete()
            .where(attraction_has_staff.c.attraction_id == attraction_id)
            .where(attraction_has_staff.c.staff_id == staff_id)
        )

        self._session.commit()