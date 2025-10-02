from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_menager import UserMenager

flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_manager = UserMenager()

users = user_manager.fetch_users()
result = flight_data.find_all_deals()
cheapest_per_dest = flight_search.find_best_deals(result)
print(cheapest_per_dest)

for deal in cheapest_per_dest:
    notification_manager.send_emails(user_data=users,data=cheapest_per_dest[deal])
    # notification_manager.generate_message(cheapest_per_dest[deal])


