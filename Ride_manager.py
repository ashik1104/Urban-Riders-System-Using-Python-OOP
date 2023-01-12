class ride_manager:
    def __init__(self):
        print('Ride manager activated')
        self.__available_cars = []
        self.__trip_history = []
        self.__available_bikes = []
        self.__available_cng = []
        self.__income = 0

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars

    def get_available_bikes(self):
        return self.__available_bikes

    def get_available_cng(self):
        return self.__available_cng
    

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            vehicles = self.__available_cars
        elif vehicle_type == 'bike':
            vehicles = self.__available_bikes
        else:
            vehicles = self.__available_cng

        if len(vehicles) == 0:
            print(f'Sorry no {vehicle_type} is available right now')
            return False
        for vehicle in vehicles:
            # print('potential', rider.location, car.driver.location)
            if abs(rider.location - vehicle.driver.location) < 10:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print('You do not enough money for this trip', fare, rider.balance)
                    return False
                if vehicle.status == 'available':
                    vehicle.status = 'unavailable'
                    # print('available cars : ', len(self.__available_cars))
                    vehicles.remove(vehicle)
                    trip_info = f'Match {vehicle_type} for {rider.name} for fare {fare} with {vehicle.driver.name} started : {rider.location} to {destination}'
                    print(trip_info)
                    rider.start_a_trip(fare, trip_info)
                    vehicle.driver.start_a_trip(rider.location, destination, fare * 0.8, trip_info)
                    self.__income += fare * 0.2
                    # print('available cars : ', len(self.__available_cars)
                    self.__trip_history.append(trip_info)
                    return True


uber = ride_manager()
