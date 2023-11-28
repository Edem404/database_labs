"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from my_project.auth.domain.orders.client import Client
from my_project.auth.domain.orders.client_type import ClientType
from my_project.auth.domain.orders.order import Order
from my_project.auth.domain.adress.region import Region
from my_project.auth.domain.adress.city import City
from my_project.auth.domain.park.park import Park
from my_project.auth.domain.park.staff import Staff
from my_project.auth.domain.orders.ticket import Ticket
from my_project.auth.domain.park.attraction import Attraction
from my_project.auth.domain.park.park_has_attraction import ParkHasAttraction
from my_project.auth.domain.park.attraction_staff import AttractionStaff
from my_project.auth.domain.orders.order_ticket import OrderTicket
