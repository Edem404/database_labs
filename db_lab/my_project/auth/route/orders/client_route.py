from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import client_controller
from my_project.auth.domain import Client

client_bp = Blueprint('clients', __name__, url_prefix='/clients')

@client_bp.get('/age_stat/<stat_type>')
def age_statistics(stat_type: str) -> Response:
    return make_response(jsonify(client_controller.age_statistics(stat_type)), HTTPStatus.OK)


@client_bp.post('/multi_insert')
def multi_insert() -> Response:
    client_controller.multi_insert()
    return make_response("unknown Inserted", HTTPStatus.CREATED)

@client_bp.post('/procedure_insertion')
def insert_client() -> Response:
    content = request.get_json()
    name = content.get("name")
    surname = content.get("surname")
    age = content.get("age")
    phone = content.get("phone")
    client_controller.insert_client(name, surname, age, phone)
    return make_response("Created", HTTPStatus.CREATED)


@client_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)


@client_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)


@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)


@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.update(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)
