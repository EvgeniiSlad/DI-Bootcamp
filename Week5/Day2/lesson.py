class Door:
    def __init__(self):
        self.is_opened = False
    
    def open_door(self):
        self.is_opened = True


    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):
    def open_door(self):
        print("Eror")


    def close_door(self):
        print("Eror")


blocked_door=BlockedDoor()
print(blocked_door.is_opened)
blocked_door.open_door()
print(blocked_door.is_opened)
