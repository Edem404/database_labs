from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import park_controller
from my_project.auth.domain import Park

park_bp = Blueprint('parks', __name__, url_prefix='/parks')


@park_bp.get('')
def get_all_parks() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(park_controller.find_all()), HTTPStatus.OK)


@park_bp.post('')
def create_park() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    park = Park.create_from_dto(content)
    park_controller.create(park)
    return make_response(jsonify(park.put_into_dto()), HTTPStatus.CREATED)


@park_bp.get('/<int:park_id>')
def get_park(park_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(park_controller.find_by_id(park_id)), HTTPStatus.OK)


@park_bp.put('/<int:park_id>')
def update_client(park_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    park = Park.create_from_dto(content)
    park_controller.update(park_id, park)
    return make_response("Park updated", HTTPStatus.OK)


@park_bp.patch('/<int:park_id>')
def patch_park(park_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    park_controller.patch(park_id, content)
    return make_response("Park updated", HTTPStatus.OK)


@park_bp.delete('/<int:park_id>')
def delete_park(park_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    park_controller.delete(park_id)
    return make_response("Park deleted", HTTPStatus.OK)
