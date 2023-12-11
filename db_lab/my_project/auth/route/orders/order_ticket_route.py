from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import order_ticket_controller
from my_project.auth.domain import OrderTicket

order_ticket_bp = Blueprint('order_tickets', __name__, url_prefix='/order_tickets')


@order_ticket_bp.get('')
def get_all_order_tickets() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(order_ticket_controller.find_all()), HTTPStatus.OK)


@order_ticket_bp.post('')
def create_order_ticket() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    order_ticket = OrderTicket.create_from_dto(content)
    order_ticket_controller.create(order_ticket)
    return make_response(jsonify(order_ticket.put_into_dto()), HTTPStatus.CREATED)


@order_ticket_bp.get('/<int:order_id>')
def get_order_ticket(order_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(order_ticket_controller.find_by_id(order_id)), HTTPStatus.OK)


@order_ticket_bp.put('/<int:order_id>')
def update_order_ticket(order_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    order_ticket = OrderTicket.create_from_dto(content)
    order_ticket_controller.update(order_id, order_ticket)
    return make_response("Order updated", HTTPStatus.OK)


@order_ticket_bp.patch('/<int:order_id>')
def patch_order_ticket(order_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    order_ticket_controller.patch(order_id, content)
    return make_response("Order updated", HTTPStatus.OK)


# @order_ticket_bp.delete('/<int:ticket_id>/<int:order_id>')
# def delete_order_ticket(ticket_id: int, order_id: int) -> Response:
#     """
#     Deletes client by ID.
#     :return: Response object
#     """
#     order_ticket_controller.delete(ticket_id, order_id)
#     return make_response("Order deleted", HTTPStatus.OK)


@order_ticket_bp.delete('/new_delete/<int:ticket_id>/<int:order_id>')
def delete_order_ticket(ticket_id: int, order_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    order_ticket_controller.delete_order_ticket(ticket_id=ticket_id, order_id=order_id)
    return make_response("Order deleted", HTTPStatus.OK)
