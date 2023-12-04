from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import staff_controller
from my_project.auth.domain import Staff

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')


@staff_bp.get('')
def get_all_staff() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(staff_controller.find_all()), HTTPStatus.OK)


@staff_bp.post('')
def create_staff() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    staff = Staff.create_from_dto(content)
    staff_controller.create(staff)
    return make_response(jsonify(staff.put_into_dto()), HTTPStatus.CREATED)


@staff_bp.get('/<int:staff_id>')
def get_staff(staff_id: int) -> Response:
    """
    Gets staff by ID.
    :return: Response object
    """
    return make_response(jsonify(staff_controller.find_by_id(staff_id)), HTTPStatus.OK)


@staff_bp.put('/<int:staff_id>')
def update_staff(staff_id: int) -> Response:
    """
    Updates staff by ID.
    :return: Response object
    """
    content = request.get_json()
    staff = Staff.create_from_dto(content)
    staff_controller.update(staff_id, staff)
    return make_response("Staff updated", HTTPStatus.OK)


@staff_bp.patch('/<int:staff_id>')
def patch_staff(staff_id: int) -> Response:
    """
    Patches staff by ID.
    :return: Response object
    """
    content = request.get_json()
    staff_controller.patch(staff_id, content)
    return make_response("Staff updated", HTTPStatus.OK)


@staff_bp.delete('/<int:staff_id>')
def delete_staff(staff_id: int) -> Response:
    """
    Deletes staff by ID.
    :return: Response object
    """
    staff_controller.delete(staff_id)
    return make_response("Staff deleted", HTTPStatus.OK)
