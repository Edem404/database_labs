
# orders DB
from .orders.client_dao import ClientDAO
from .orders.client_type_dao import ClientTypeDAO
from .orders.order_dao import OrderDAO
from .adress.region_dao import RegionDAO
from .adress.city_dao import CityDAO
from .park.park_dao import ParkDAO
from .park.staff_dao import StaffDAO
from .orders.ticket_dao import TicketDAO
from .park.attraction_dao import AttractionDAO
from .park.park_has_attraction_dao import ParkHasAttractionDAO
from .park.attraction_staff_dao import AttractionStaffDAO
from .orders.order_ticket_dao import OrderTicketDAO

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
order_dao = OrderDAO()

region_dao = RegionDAO()
city_dao = CityDAO()
park_dao = ParkDAO()
staff_dao = StaffDAO()
ticket_dao = TicketDAO()
attraction_dao = AttractionDAO()
park_has_attraction_dao = ParkHasAttractionDAO()
attraction_staff_dao = AttractionStaffDAO()
order_ticket_dao = OrderTicketDAO()
