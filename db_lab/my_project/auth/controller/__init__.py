from .orders.client_controller import ClientController
from .orders.client_type_controller import ClientTypeController
from .orders.order_controller import OrderController
from .adress.region_controller import RegionController
from .adress.city_controller import CityController
from .park.park_controller import ParkController
from .park.staff_controller import StaffController
from .orders.ticket_controller import TicketController
from .park.attraction_controller import AttractionController
from .park.park_has_attraction_controller import ParkHasAttractionController
from .park.attraction_staff_controller import AttractionStaffController
from .orders.order_ticket_controller import OrderTicketController

client_controller = ClientController()
client_type_controller = ClientTypeController()
order_controller = OrderController()

region_controller = RegionController()
city_controller = CityController()
park_controller = ParkController()
staff_controller = StaffController()
ticket_controller = TicketController()
attraction_controller = AttractionController()
park_has_attraction_controller = ParkHasAttractionController()
attraction_staff_controller = AttractionStaffController()
order_ticket_controller = OrderTicketController()
