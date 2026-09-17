import time
class elevator:
    def __init__(self, floor = 0, door = False):
        self.floor = floor
        self.door = door

    def openDoor(self, open):
            if open == True:
                print("Abrindo a porta")
                time.sleep(2)
                self.door = open

    def rideElevator(self, currentFloor):
        if self.floor >=  0 and self.floor <= 20 and self.door == True:
            print("Fechando a porta")
            self.door = False
            time.sleep(2)
            if self.floor < currentFloor:
                print("Subindo ⬆️")
                time.sleep(2)
            elif self.floor > currentFloor:
                print("Descendo ⬇️")
                time.sleep(2)
            self.floor = currentFloor
            print("Abrindo a porta")
            self.door = True
            time.sleep(3)
            print("Fechando a porta")
            self.door = False
            
people = elevator()
people.openDoor()
people.rideElevator(20)
