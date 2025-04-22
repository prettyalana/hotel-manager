class Hotel:
    def __init__(self):
        self.hotel = {
            "1": {
                "101": ["George Jefferson", "Wheezy Jefferson"],
            },
            "2": {
                "237": ["Jack Torrance", "Wendy Torrance"],
            },
            "3": {"333": ["Neo", "Trinity", "Morpheus"]},
        }

    def check_in_check_out(self):
        floor_number = input(
            "Choose a floor number: Floor 1: Room 101, Floor 2: Room 237, or Floor 3: Room 333  "
        )
        room_number = input(
            "Choose a room number: Room 101: Floor 1, Room 237: Floor 2, or Room 333: Floor 3 "
        )
        return floor_number, room_number

    def is_checking_in(self):
        occupants = input("How many occupants? ")
        occupant_names = input("What are the occupant's names? ")
        print(occupants, occupant_names)
        return occupant_names

    def add_guest(self):
        floor, room = self.check_in_check_out()
        # Check if the floor and room the user provided is in the hotel
        if floor in self.hotel and room in self.hotel[floor]:
            # If the room is not occupied check the user in
            if len(self.hotel[floor][room]) == 0:
                occupant_names = self.is_checking_in()
                self.hotel[floor][room] = occupant_names.split(", ")
                print(f"{occupant_names} have been checked into {room, floor}")
            else:
                print(f"Room: {room} is already occupied.")
        else:
            print("That room does not exist.")

    def remove_guest(self):
        floor, room = self.check_in_check_out()
        # Check if the floor and room the user provided is in the hotel
        if floor in self.hotel and room in self.hotel[floor]:
            # If the room is occupied check the user out
            if len(self.hotel[floor][room]) > 0:
                delete_guest = self.hotel[floor][room]
                self.hotel[floor][room] = []
                print(f"{delete_guest} has checked out.")
        else:
            print("That room does not exist.")

    def display_occupants_and_rooms(self):
        print(self.hotel)

    def guest_status_menu(self):
        tries = 3
        while tries > 0:
            guest_input = input("Are you checking in or out? ")

            if guest_input == "in":
                self.add_guest()
                self.display_occupants_and_rooms()
            elif guest_input == "out":
                self.remove_guest()
                self.display_occupants_and_rooms()
            else:
                tries -= 1
                print("Please choose in or out")
                if tries == 0:
                    print(
                        "You have input an invalid option too many times. Try again later."
                    )
                    break


hollywood_hotel = Hotel()
hollywood_hotel.guest_status_menu()
