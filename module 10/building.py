from elevator import Elevator

class Building:
    def __init__(self,bottom,top,num):
        self.bottom_floor= bottom
        self.top_floor= top
        self.num_of_elevators= num
        self.elevators=[]
        for i in range(self.num_of_elevators):
            self.elevators.append(Elevator(self.bottom_floor,self.top_floor))

    def run_elevators(self,num,destination_floor):
        if num < 1 or num > self.num_of_elevators:
            print(f"Invalid elevator number")
            return
        print(f'Moving Elevator {num}')
        self.elevators[num-1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print(" Fire alarm activated, Please move to the bottom floor!")
        for i, elevator in enumerate(self.elevators, start = 1):
            print(f"Moving elevator {i} to the bottom floor.")
            elevator.go_to_floor(self.bottom_floor)
