import os
import csv

class CarBase:
    
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        if body_whl != "":
            self.body_length, self.body_width, self.body_height = [float(x) for x in body_whl.split('x')]
        else:
            self.body_length, self.body_width, self.body_height = 0,0,0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height
    


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            #print(row)
            if len(row) == 7:
                type_car = row[0]
                brand = row[1]
                passanger_seats_count = row[2]
                if passanger_seats_count != "":
                    passanger_seats_count = int(passanger_seats_count)
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                if carrying != "":
                    carrying = float(carrying)
                extra = row[6]
                if type_car == 'car':
                    car_list.append(Car(brand, photo_file_name, carrying, passanger_seats_count))
                elif type_car == 'truck':
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif type_car == 'spec_machine':
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
                else:
                    pass
    return car_list            