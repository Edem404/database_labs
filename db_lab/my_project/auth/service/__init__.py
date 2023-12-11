from .orders.client_service import ClientService
from .orders.client_type_service import ClientTypeService
from .orders.order_service import OrderService
from .adress.region_service import RegionService
from .adress.city_service import CityService
from .park.park_service import ParkService
from .park.staff_service import StaffService
from .orders.ticket_service import TicketService
from .park.attraction_service import AttractionService
from .park.park_has_attraction_service import ParkHasAttractionService
from .park.attraction_staff_service import AttractionStaffService
from .orders.order_ticket_service import OrderTicketService

client_service = ClientService()
client_type_service = ClientTypeService()
order_service = OrderService()

region_service = RegionService()
city_service = CityService()
park_service = ParkService()
staff_service = StaffService()
ticket_service = TicketService()
attraction_service = AttractionService()
park_has_attraction_service = ParkHasAttractionService()
attraction_staff_service = AttractionStaffService()
order_ticket_service = OrderTicketService()
