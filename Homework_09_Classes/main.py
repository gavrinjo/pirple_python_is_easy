#lab
class Vehicle:

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.maintenance = False
        self.sinceMaintenance = 0

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def NeedsMaintenance(self):
        if self.sinceMaintenance >= 100:
            self.maintenance = True
        else:
            self.maintenance = False

    def TripsSinceMaintenance(self):
        self.sinceMaintenance = 0

    def Repair(self):
        self.maintenance = False
        self.sinceMaintenance = 0
        print("Vehicle is being repaired!\n")


class Cars(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isdriving = False
        self.distance = 0

    def Drive(self, distance):
        self.isdriving = True
        self.distance = distance

    def Stop(self):
        if self.isdriving:
            self.sinceMaintenance += self.distance
            self.isdriving = False
            self.NeedsMaintenance()

    def __str__(self):
        return f"Make: {self.make} | Model: {self.model} | Manufactured: {self.year}. | Weight: {self.weight}kg\n" \
               f"Mileage Since Last Maintenance: {self.sinceMaintenance}km\n" \
               f"Needs Maintenance: {self.maintenance}\n"


class Planes(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isflyng = False
        self.distance = 0

    def Flying(self, distance):
        self.isflyng = True
        self.distance = distance
        if self.maintenance:
            print("Plane can't fly until it's repaired... Safety first!!\n")

    def Landing(self):
        if self.isflyng:
            self.sinceMaintenance += self.distance
            self.isflyng = False
            self.NeedsMaintenance()

    def __str__(self):
        return f"Make: {self.make} | Model: {self.model} | Manufactured: {self.year}. | Weight: {self.weight}kg\n" \
               f"Mileage Since Last Maintenance: {self.sinceMaintenance}km\n" \
               f"Needs Maintenance: {self.maintenance}\n"


c1 = Cars("opel", "astra", 2018, 1500)
c2 = Cars("BMW", "320d", 2016, 1600)
c3 = Cars("Mercedes", "B200cdi", 2005, 1550)

print(c1)
c1.Drive(90)
c1.Stop()
c1.Drive(50)
c1.Stop()
c1.Repair()
print(c1)

print(c2)
c2.Drive(70)
c2.Stop()
c2.Drive(60)
c2.Stop()
c2.Repair()
c2.Drive(50)
c2.Stop()
print(c2)

print(c3)
c3.Drive(70)
c3.Stop()
c3.Drive(150)
c3.Stop()
c3.Repair()
c3.Drive(30)
c3.Stop()

p1 = Planes("boeing", "747", 1995, 183500)

print(p1)
p1.Flying(150)
p1.Landing()
p1.Flying(20)
p1.Repair()
p1.Flying(30)
p1.Landing()
print(p1)
