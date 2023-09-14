class Vehicle:
    # Initializer
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Methods
    def moves(self):
        print('Moves along..')

    # Getter
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# # print(my_car.make)  # Tesla
# # print(my_car.model)  # Model 3
# my_car.get_make_model()  # I'm a Tesla Model 3.
# my_car.moves()  # Moves along..

your_car = Vehicle('Cadillac', 'Escalade')
# your_car.get_make_model()  # I'm a Cadillac Escalade.
# your_car.moves()  # Moves along..

# ======= Inheritance =======


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()  # I'm a Cessna Skyhawk.
cessna.moves()  # Flies along..
mack.get_make_model()  # I'm a Mack Pinnacle.
mack.moves()  # Rumbles along..
golfwagon.get_make_model()  # I'm a Yamaha GC100.
golfwagon.moves()  # Moves along..

# ======= Ploymorphism =======

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()

# I'm a Tesla Model 3.
# Moves along..
# I'm a Cadillac Escalade.
# Moves along..
# I'm a Cessna Skyhawk.
# Flies along..
# I'm a Mack Pinnacle.
# Rumbles along..
# I'm a Yamaha GC100.
# Moves along..
