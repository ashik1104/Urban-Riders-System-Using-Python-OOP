from abc import ABC, abstractmethod
import time
import threading


class vehicle(ABC):
    speeds = {'car': 30, 'bike': 50, 'cng': 40}

    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.driver = driver
        self.speed = vehicle.speeds[vehicle_type]
        self.status = 'available'

    @abstractmethod
    def start_driving(self, start, destination):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance = abs(start - destination)
        for i in range(distance):
            time.sleep(0.5)
            print(f'Driving {self.license_plate} current position : {i} of {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')


class bike(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance = abs(start - destination)
        for i in range(distance):
            time.sleep(0.5)
            print(f'Driving {self.license_plate} current position : {i} of {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')


class cng(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance = abs(start - destination)
        for i in range(distance):
            time.sleep(0.5)
            print(f'Driving {self.license_plate} current position : {i} of {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')
