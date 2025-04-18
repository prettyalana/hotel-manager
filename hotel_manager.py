hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

def check_in_check_out() :
    floor_number = input("Choose a floor number: Floor 1: Room 101, Floor 2: Room 237, or Floor 3: Room 333  ")
    room_number = input("Choose a room number: Room 101: Floor 1, Room 237: Floor 2, or Room 333: Floor 3 ")
    return floor_number, room_number

def is_checking_in() :
    occupants = input("How many occupants? ")
    occupant_names = input("What are the occupant's names? ")
    print(occupants, occupant_names)
    return occupant_names
        
def add_guest() :
    floor, room = check_in_check_out()
    occupant_names = is_checking_in()
    hotel[floor][room] = occupant_names.split(", ")
    print(f"{occupant_names} Have been checked into {room, floor}")
    
def remove_guest() :
    floor, room = check_in_check_out()
    delete_guest = hotel[floor].pop(room)
    print(delete_guest)
    
def display_occupants_and_rooms() :
    print(hotel)

def guest_status_menu():
    guest_input = input("Are you checking in or out? ")
    if guest_input == "in" :
        add_guest()
        display_occupants_and_rooms()
        exit()
    elif guest_input == "out" :
        remove_guest()
        display_occupants_and_rooms()
    else :
        print(f"Please choose in or out")
                
guest_status_menu()
    
 
 
 
 