class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.deals = []
        self.cheapest_per_dest = {}

    def find_best_deals(self,deals):
        self.deals = deals

        for offer in self.deals:
            price = float(offer["price"]["total"])
            first_segment = offer["itineraries"][0]["segments"]
            last_segment = offer["itineraries"][1]["segments"]
            destination = first_segment[-1]["arrival"]["iataCode"]

            if destination not in self.cheapest_per_dest or price < self.cheapest_per_dest[destination]["price"]:
                self.cheapest_per_dest[destination] = {
                    "price": price,
                    "date": first_segment[0]["departure"]["at"],
                    "currency": offer["price"]["currency"],
                    "from": offer["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    "to": destination,
                    "until": last_segment[0]["arrival"]["at"],
                    "id": offer["id"]
                }

        return self.cheapest_per_dest





