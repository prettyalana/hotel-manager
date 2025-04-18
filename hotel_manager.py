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
    # Check if the floor and room the user provided is in the hotel 
    if floor in hotel and room in hotel[floor] :
      # If the room is not occupied check the user in
      if len(hotel[floor][room]) == 0 :
        occupant_names = is_checking_in()
        hotel[floor][room] = occupant_names.split(", ")
        print(f"{occupant_names} have been checked into {room, floor}")
      else :
        print(f"Room: {room} is already occupied.")
    else :
      print("That room does not exist.")
    
def remove_guest() :
    floor, room = check_in_check_out()
    # Check if the floor and room the user provided is in the hotel 
    if floor in hotel and room in hotel[floor] :
      # If the room is occupied check the user out
      if len(hotel[floor][room]) > 0 :
        delete_guest = hotel[floor][room]
        hotel[floor][room] = []
        print(f"{delete_guest} has checked out.")
    else :
      print("That room does not exist.")
    
def display_occupants_and_rooms() :
    print(hotel)

def guest_status_menu():
    while True:
      guest_input = input("Are you checking in or out? ")
     
      if guest_input == "in" :
          add_guest()
          display_occupants_and_rooms()
      elif guest_input == "out" :
          remove_guest()
          display_occupants_and_rooms()
      else :
          print(f"Please choose in or out")
                  
guest_status_menu()
    
 
 
 
 