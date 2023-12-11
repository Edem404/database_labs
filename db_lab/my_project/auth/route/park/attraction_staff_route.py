from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import attraction_staff_controller
from my_project.auth.domain import AttractionStaff

attraction_staff_bp = Blueprint('attraction_staff', __name__, url_prefix='/attraction_staff')


@attraction_staff_bp.get('')
def get_all_attraction_staff() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(attraction_staff_controller.find_all()), HTTPStatus.OK)


@attraction_staff_bp.post('')
def create_attraction_staff() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    attraction_staff = AttractionStaff.create_from_dto(content)
    attraction_staff_controller.create(attraction_staff)
    return make_response(jsonify(attraction_staff.put_into_dto()), HTTPStatus.CREATED)


@attraction_staff_bp.get('/<int:attraction_id>')
def get_attraction_staff(attraction_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(attraction_staff_controller.find_by_id(attraction_id)), HTTPStatus.OK)


@attraction_staff_bp.put('/<int:attraction_id>')
def update_attraction_staff(attraction_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    client = AttractionStaff.create_from_dto(content)
    attraction_staff_controller.update(attraction_id, client)
    return make_response("AttractionStaff updated", HTTPStatus.OK)


@attraction_staff_bp.patch('/<int:attraction_id>')
def patch_attraction_staff(attraction_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    attraction_staff_controller.patch(attraction_id, content)
    return make_response("AttractionStaff updated", HTTPStatus.OK)


@attraction_staff_bp.delete('/<int:attraction_id>')
def delete_attraction_staff(attraction_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    attraction_staff_controller.delete(attraction_id)
    return make_response("AttractionStaff deleted", HTTPStatus.OK)


@attraction_staff_bp.get('/<int:staff_id>/attractions')
def find_attractions_by_staff_id(staff_id: int) -> Response:
    return make_response(jsonify(attraction_staff_controller.find_attractions_by_staff_id(staff_id)), HTTPStatus.OK)
