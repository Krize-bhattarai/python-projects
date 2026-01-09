class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} is driving.')

    def paint(self, new_color):
        self.color = new_color
        print(f'{self.brand} is now {self.color}.')

my_car = car("Toyota", "Red")  # create an object
my_car.drive()                  # call a function → Toyota is driving.
my_car.paint("Blue")            # change color → Toyota is now Blue.
   