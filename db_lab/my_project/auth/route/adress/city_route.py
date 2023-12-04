from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import city_controller, region_controller
from my_project.auth.domain import City

city_bp = Blueprint('cities', __name__, url_prefix='/cities')


@city_bp.get('')
def get_all_cities() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)


@city_bp.post('')
def create_city() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)


@city_bp.get('/<string:city_id>')
def get_client(city_id: str) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(city_controller.find_by_id(city_id)), HTTPStatus.OK)


@city_bp.put('/<string:city_id>')
def update_client(city_id: str) -> Response:
    """
    Updates region by ID.
    :return: Response object
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.patch('/<string:city_id>')
def patch_client(city_id: str) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    city_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.delete('/<string:city_id>')
def delete_client(city_id: str) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    city_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)


city_in_region_bp = Blueprint('cities_in_region', __name__, url_prefix='/regions/<string:region_id>/cities')


@city_in_region_bp.get('')
def get_cities_in_region(region_id: str) -> Response:
    """
    Gets all cities in a specific region.
    :return: Response object
    """
    region = region_controller.find_by_id(region_id)
    if region:
        cities = region['cities']
        return make_response(jsonify(cities), HTTPStatus.OK)
    # else:
    #     return make_response("Region not found", HTTPStatus.NOT_FOUND)
