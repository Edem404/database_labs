from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import attraction_controller
from my_project.auth.domain import Attraction

attraction_bp = Blueprint('attractions', __name__, url_prefix='/attractions')


@attraction_bp.post('/insert')
def insert_attraction_has_staff():
    content = request.get_json()
    staff_name = content.get("staff_name")
    staff_surname = content.get("staff_surname")
    attraction_name = content.get("attraction_name")

    attraction_controller.insert_attraction_has_staff(staff_name, staff_surname, attraction_name)
    return make_response("create relationship", HTTPStatus.CREATED)

@attraction_bp.post('/<int:attraction_id>/add_staff')
def add_car_to_order(attraction_id) -> Response:
    staff_id = request.get_json().get('staff_id')

    return make_response(jsonify(attraction_controller.add_staff_to_attraction(attraction_id, staff_id)), HTTPStatus.OK)


@attraction_bp.get('/<int:attraction_id>/staff')
def get_all_staff_in_attraction(attraction_id) -> Response:
    return make_response(jsonify(attraction_controller.find_staff_in_attraction(attraction_id)), HTTPStatus.OK)


@attraction_bp.delete('/<int:attraction_id>/delete_staff_from_attraction')
def delete_staff_from_attraction(attraction_id) -> Response:
    staff_id = request.get_json().get('staff_id')
    return make_response(jsonify(attraction_controller.delete_staff_from_attraction(attraction_id, staff_id)), HTTPStatus.OK)


@attraction_bp.get('')
def get_all_attractions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(attraction_controller.find_all()), HTTPStatus.OK)


@attraction_bp.post('')
def create_attraction() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    attraction = Attraction.create_from_dto(content)
    attraction_controller.create(attraction)
    attraction_id = attraction.id
    staff_id = content.get('staff_id')
    attraction_controller.add_staff_to_attraction(attraction_id, staff_id)
    return make_response(jsonify(attraction.put_into_dto()), HTTPStatus.CREATED)


@attraction_bp.get('/<int:attraction_id>')
def get_attraction(attraction_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(attraction_controller.find_by_id(attraction_id)), HTTPStatus.OK)


@attraction_bp.put('/<int:attraction_id>')
def update_attraction(attraction_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    client = Attraction.create_from_dto(content)
    attraction_controller.update(attraction_id, client)
    return make_response("Attraction updated", HTTPStatus.OK)


@attraction_bp.patch('/<int:attraction_id>')
def patch_attraction(attraction_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    attraction_controller.patch(attraction_id, content)
    return make_response("Attraction updated", HTTPStatus.OK)


@attraction_bp.delete('/<int:attraction_id>')
def delete_attraction(attraction_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    attraction_controller.delete(attraction_id)
    return make_response("Attraction deleted", HTTPStatus.OK)
