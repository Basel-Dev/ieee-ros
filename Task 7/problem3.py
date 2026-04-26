class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger_obj):
        if isinstance(passenger_obj, Passenger):
            self.passengers.append(passenger_obj)


coolest_passenger_ever = Passenger("Razan")
also_coolest_passenger_ever = Passenger("Maisoon")

coolest_flight_ever = Flight()

coolest_flight_ever.add_passenger(coolest_passenger_ever)
coolest_flight_ever.add_passenger(also_coolest_passenger_ever)

print([passenger.name for passenger in coolest_flight_ever.passengers])
    