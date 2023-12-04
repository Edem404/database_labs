from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import park_has_attraction_controller
from my_project.auth.domain import ParkHasAttraction

park_has_attraction_bp = Blueprint('park_has_attractions', __name__, url_prefix='/park_has_attractions')


@park_has_attraction_bp.get('')
def get_all_park_has_attractions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(park_has_attraction_controller.find_all()), HTTPStatus.OK)


@park_has_attraction_bp.post('')
def create_park_has_attraction() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    park_has_attraction = ParkHasAttraction.create_from_dto(content)
    park_has_attraction_controller.create(park_has_attraction)
    return make_response(jsonify(park_has_attraction.put_into_dto()), HTTPStatus.CREATED)


@park_has_attraction_bp.get('/<int:attraction_id>')
def get_park_has_attraction(attraction_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(park_has_attraction_controller.find_by_id(attraction_id)), HTTPStatus.OK)


@park_has_attraction_bp.put('/<int:attraction_id>')
def update_park_has_attraction(attraction_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    client = ParkHasAttraction.create_from_dto(content)
    park_has_attraction_controller.update(attraction_id, client)
    return make_response("ParkHasAttraction updated", HTTPStatus.OK)


@park_has_attraction_bp.patch('/<int:attraction_id>')
def patch_park_has_attraction(attraction_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    park_has_attraction_controller.patch(attraction_id, content)
    return make_response("ParkHasAttraction updated", HTTPStatus.OK)


@park_has_attraction_bp.delete('/<int:attraction_id>')
def delete_park_has_attraction(attraction_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    park_has_attraction_controller.delete(attraction_id)
    return make_response("ParkHasAttraction deleted", HTTPStatus.OK)
