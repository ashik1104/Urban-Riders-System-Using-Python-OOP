import hashlib
import random

from Brta import BRTA
from Vehicle import *
from Ride_manager import uber
import threading


license_authority = BRTA()


class user:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('user.txt', 'a') as file:
            with open('user.txt', 'r') as chk:
                content = chk.read()
            if self.email not in content:
                file.write(f'{email} {pwd_encrypted}\n')

        file.close()
        chk.close()
        # print(f'{self.name} user created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        if hashed_pass == stored_password:
            print('Valid user')
            return True
        else:
            print('Invalid user')
            return False


class Rider(user):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        self.__trip_history = []

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self):
        pass

    def start_a_trip(self, fare, trip_info):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)

    def get_history(self):
        return self.__trip_history


class Driver(user):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.__trip_history = []
        self.earning = 0
        self.vehicle = None

    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if not result:
            # print('sorry you failed. Try again')
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver:
            if vehicle_type == 'car':
                self.vehicle = car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
        else:
            # print('You are not a valid driver')
            pass

    def start_a_trip(self, start, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        self.__trip_history.append(trip_info)
        # start thread
        trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start, destination)
        


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1*#', random.randint(0, 100), 1000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2*#', random.randint(0, 100), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3*#', random.randint(0, 100), 5000)
rider4 = Rider('rider4', 'rider4@gmail.com', 'rider4*#', random.randint(0, 100), 5000)

for i in range(1, 21):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}*#', random.randint(0, 100),
                     random.randint(1000, 9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(random.choice(['car', 'bike', 'cng']), random.randint(10000, 99999), 10)


print(uber.get_available_cars())
print(uber.get_available_bikes())
print(uber.get_available_cng())

uber.find_a_vehicle(rider1, random.choice(['car', 'bike', 'cng']), random.randint(1, 100))
uber.find_a_vehicle(rider2, random.choice(['car', 'bike', 'cng']), random.randint(1, 100))
uber.find_a_vehicle(rider3, random.choice(['car', 'bike', 'cng']), random.randint(1, 100))
uber.find_a_vehicle(rider4, random.choice(['car', 'bike', 'cng']), random.randint(1, 100))


print(uber.total_income())


