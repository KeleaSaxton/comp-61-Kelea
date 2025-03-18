
class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        pass

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"
    pass

class Owner:
    def __init__(self, name, age):
       self.name = name 
       self.age = age
       self.cars_owned = []
    pass

    def purchase_car(self, car):
        self.cars_owned.append(car)
        print(f'{self.name} just purchased a {car.get_car_info()}')
        pass

    def show_owned_cars(self):
        if not self.cars_owned: 
            print(f"{self.name} doesn't own any cars yet")
        else: 
            print(f"{self.name} owns the following cars:")
            for car in self.cars_owned: 
                print(f"- {car.get_car_info()}")
        pass


def main():
    owner1 = Owner('Paul', 20)
    owner2 = Owner('Amy', 21)
    car1 = Car('Toyota', 'Tacoma', 2009)
    car2 = Car('Volkswagon', 'West Falia', 2009)
    car3 = Car('Toyota', 'Tundra', 2014)
    car4 = Car('Ford', 'F150', 2019)
    owner1.purchase_car(car1)
    owner1.purchase_car(car4)

    owner2.purchase_car(car2)
    owner2.purchase_car(car3)

    owner1.show_owned_cars()
    owner2.show_owned_cars()
    pass

if __name__ == "__main__":
    main()