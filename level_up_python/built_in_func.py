class Car:
    def __init__(self):
        self.wheels = 4

    def drive(self):
        print("drive")


mycar = Car()

print(hasattr(mycar, "wheels"))
print(hasattr(mycar, "drive"))

getattr(mycar, "wheels")
method = getattr(mycar, "drive")
method()
