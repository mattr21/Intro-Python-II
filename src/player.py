# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    # Brady's way
    def travel(self, direction):
        next_room = self.current_room.getRoomDirection(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print(f"\n------------------------------------\nThere's a wall in that direction!\n------------------------------------\n")
    
    
    
    
    



    # Yanrong's way with getattr()
    # def move_direction(self, direction):
    #     if getattr(self.current_room, f"{direction}_to") != None:
    #         self.current_room = getattr(self.current_room, f"{direction}_to")
    #     else:
    #         print("There's a wall in that direction!")