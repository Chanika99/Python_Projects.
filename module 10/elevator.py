class Elevator:
    def __init__(self, bottom,top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def go_to_floor(self,target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print('Invalid floor')
            return
        while target_floor > self.current_floor:
                self.floor_up()
        while target_floor < self.current_floor:
                self.floor_down()

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f'Current Floor: {self.current_floor}')

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f'Current Floor: {self.current_floor}')



