# Princess Sampson
# Dr. Lawrence - Python II
# Vehicle class hierachy

# The Automobile class holds general data about an automobile in inventory.
class Automobile:
    # The __init__ method accepts arguments for the make, model, mileage, and price.
   # it initializes  the data attributes with these values.
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    # The following methods are mutators for the class's data attributes.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The following methods are the accessors for the class's data attributes.
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    #This is the str method for the automobile's make, model, mileage, price.
    def __str__(self):
        return '%s %s | %s mileage| $%d' % (self.get_make(), self.get_model(), self.get_mileage(), self.get_price())

# The Car class represents a car. It is a subclass
# of the Automobile class.
class Car(Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.

    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the __doors attribute.
        self.__doors = doors
    # The set_doors method is the mutator for the  __doors attribute.

    def set_doors(self, doors):
        self.__doors = doors
    # The get_doors method is the accessor for the
    # __doors attribute.

    def get_doors(self):
        return self.__doors

    #This is the str method for the car's make, model, mileage, price, and doors.
    def __str__(self):
        automobile_info = Automobile.__str__(self)
        car_info = ' | %d door(s)' % (self.get_doors())

        return automobile_info + car_info


# The Truck class represents a pickup truck. It is a subclass of the Automobile class
class Truck(Automobile):
    # The __init__ method accepts arguments for the
    # truck's make, model, mileage, price, and drive type.

    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the __drive_type attribute.
        self.__drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # __drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # The get_drive_type method is the accessor for the
    # __drive_type attribute.
    def get_drive_type(self):
        return self.__drive_type

    #This is the str method for the truck's make, model, mileage, price, and drive_type.
    def __str__(self):
        automobile_info = Automobile.__str__(self)
        truck_info = ' | %d-wheel drive' % (self.get_drive_type())

        return automobile_info + truck_info

# The SUV class represents a sport utility vehicle. It is a subclass of the Automobile class.
class SUV(Automobile):
    # The __init__ method caccepts arguments for the
    # SUV's make, model, mileage, price, and passenger capacity.
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap

    # The set_pass_cap method is the mutator for the
    # __pass_cap attribute.
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap
    
    # The get_pass_cap method is the accessor for the
    # __pass_cap attribute.
    def get_pass_cap(self):
        return self.__pass_cap

    #This is the str method for the SUV's make, model, mileage, price, and passenger capacity.
    def __str__(self):
        automobile_info = Automobile.__str__(self)
        suv_info = ' | Seats %d' % (self.get_pass_cap())

        return automobile_info + suv_info

# The train class represents a train. It is a subclass of the Automobile class.
class Train(Automobile):
    # The __init__ method caccepts arguments for the
    # Train's make, model, mileage, price, passenger capacity, and no. of cars attached.
    def __init__(self, make, model, mileage, price, cars):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        # Initialize the cars attribute.
        self._cars = cars

    # The set_cars method is the mutator for the
    # _cars attribute.
    def set_cars(self, cars):
        self._cars = cars
    
    # The get_cats method is the accessor for the
    # _cars attribute.
    def get_cars(self):
        return self._cars

    #This is the str method for the train's make, model, mileage, price, and cars attached.
    def __str__(self):
        automobile_info = Automobile.__str__(self)
        train_info = ' | %d car(s) attached' % (self.get_cars())

        return automobile_info + train_info
    
