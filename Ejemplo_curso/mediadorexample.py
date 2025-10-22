from abc import ABC, abstractmethod

class IAirTrafficControl(ABC):
    @abstractmethod
    def send_message(self, sender, message):
        pass

    @abstractmethod
    def register_aircraft(self, aircraft):
        pass

class Aircraft(ABC):
    def __init__(self, tower: IAirTrafficControl, name: str):
        self.tower = tower
        self.name = name
        tower.register_aircraft(self)

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass

class Airplane(Aircraft):
    def send_message(self, message):
        print(f"Airplane {self.name} is sending: '{message}'")
        self.tower.send_message(self, message)

    def receive_message(self, message):
        print(f"Airplane {self.name} received message: '{message}'")

class Helicopter(Aircraft):
    def send_message(self, message):
        print(f"Helicopter {self.name} is sending: '{message}'")
        self.tower.send_message(self, message)

    def receive_message(self, message):
        print(f"Helicopter {self.name} received message: '{message}'")

class Tower(IAirTrafficControl):
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        if aircraft not in self.aircrafts:
            self.aircrafts.append(aircraft)
            print(f"Tower registered: {aircraft.name}")

    def send_message(self, sender, message):
        for aircraft in self.aircrafts:
            if aircraft is not sender:
                aircraft.receive_message(message)

if __name__ == "__main__":
    tower = Tower()

    airplane1 = Airplane(tower, "Airplaine1")
    airplane2 = Airplane(tower, "Airplane2")
    helicopter1 = Helicopter(tower, "Helicopter1")

    airplane1.send_message("Hello from Airplane1!")
