from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import region_controller
from my_project.auth.domain import Region
from my_project.auth.domain import City
region_bp = Blueprint('regions', __name__, url_prefix='/regions')


@region_bp.get('')
def get_all_regions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)

@region_bp.post('create_region_and_many_cities')
def create_region_and_many_cities() -> Response:
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_name = region.name
    cities = content.get("cities_in_region")
    region_controller.create_region_and_many_cities(region_name, cities)
    return make_response()


@region_bp.post('')
def create_region() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.CREATED)


@region_bp.get('/<int:region_id>')
def get_client(region_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_by_id(region_id)), HTTPStatus.OK)


@region_bp.put('/<int:region_id>')
def update_client(region_id: int) -> Response:
    """
    Updates region by ID.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.update(region_id, region)
    return make_response("Region updated", HTTPStatus.OK)


@region_bp.patch('/<int:region_id>')
def patch_client(region_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    region_controller.patch(region_id, content)
    return make_response("Region updated", HTTPStatus.OK)


@region_bp.delete('/<int:region_id>')
def delete_client(region_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    region_controller.delete(region_id)
    return make_response("Region deleted", HTTPStatus.OK)

@region_bp.get('/<string:region_id>/citiess')
def find_cities_by_index(region_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_cities_by_index(region_id)), HTTPStatus.OK)
