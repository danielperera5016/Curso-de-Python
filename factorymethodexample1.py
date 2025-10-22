from abc import ABC,abstractmethod

class Ivehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass 

    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.star()
        vehicle.drive()
        vehicle.stop()

        return vehicle
    
class Bike(Ivehicle):
        def drive(self):
             print("Riding the bike.")

        def start(self):
             print("Starting the bike.")

        def stop(self):
             print("Stopping the bike.")
             
