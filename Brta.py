import random


class BRTA:
    def __init__(self):
        self.__license = {}

    def driving_test(self, email):
        score = random.randint(0, 101)
        if score >= 33:
            # print('congrats, you have passed', score)
            license_number = random.randint(50000, 99999)
            self.__license[email] = license_number
            return license_number
        else:
            # print('sorry you failed', score)
            return False

    def validate_license(self, email, license):
        for key, val in self.__license.items():
            if key == email and val == license:
                return True
        return False
