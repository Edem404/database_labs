from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    # from .orders.client_type_route import client_type_bp
    from .orders.order_route import order_bp
    from .adress.region_route import region_bp
    from .adress.city_route import city_bp
    from .park.park_route import park_bp
    from .park.staff_route import staff_bp
    from .orders.ticket_route import ticket_bp
    from .park.attraction_route import attraction_bp
    from .park.park_has_attraction_route import park_has_attraction_bp
    from .park.attraction_staff_route import attraction_staff_bp
    from .orders.order_ticket_route import order_ticket_bp
    from .adress.city_route import city_in_region_bp

    app.register_blueprint(client_bp)
    # app.register_blueprint(client_type_bp)

    app.register_blueprint(order_bp)

    app.register_blueprint(region_bp)

    app.register_blueprint(city_bp)

    app.register_blueprint(park_bp)

    app.register_blueprint(staff_bp)

    app.register_blueprint(ticket_bp)

    app.register_blueprint(attraction_bp)

    app.register_blueprint(park_has_attraction_bp)

    app.register_blueprint(attraction_staff_bp)

    app.register_blueprint(order_ticket_bp)

    app.register_blueprint(city_in_region_bp)
