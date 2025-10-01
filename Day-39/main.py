from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

result = flight_data.find_all_deals()
cheapest_per_dest = flight_search.find_best_deals(result)
print(cheapest_per_dest)

for deal in cheapest_per_dest:
    notification_manager.generate_message(cheapest_per_dest[deal])


