class Hotel:
    def __init__(self, name):
        self.name = name
        self.hotel_data = { 
            1: {
                101: ["George Jefferson", "Wheezy Jefferson"],
            },
            2: {
                237: ["Jack Torrance", "Wendy Torrance"],
            },
            3: {333: ["Neo", "Trinity", "Morpheus"]},
        }

    def welcome_message(self):
        print(f"Welcome to {self.name}.")

    def check_in_check_out(self):
        
        while True: 
            try:
                floor_number = int(
                    input("Choose a floor number: Floor 1, Floor 2, or Floor 3 ")
                )
                # Check if input is an integer
                if isinstance(floor_number, int): 
                    room_number = int(
                        input("Choose a room number: Room 101, Room 237, or Room 333 ")
                    )
                return floor_number, room_number
            except ValueError:
                print("Please input a whole number.")

    def is_checking_in(self):
        occupants = int(input("How many occupants? "))
        if occupants > 1:
            occupant_names = input("What are the occupant's names? ")
        else:
            occupant_names = input("What is the occupant's name? ")

        print(f"{occupants}: {occupant_names}")
        return occupants, occupant_names

    def add_guest(self):
        floor, room = self.check_in_check_out()
        # Check if the floor and room the user provided is in the hotel
        if floor in self.hotel_data and room in self.hotel_data[floor]:
            # If the room is not occupied check the user in
            if len(self.hotel_data[floor][room]) == 0:
                occupant, occupant_names = self.is_checking_in()
                self.hotel_data[floor][room] = occupant_names.split(", ")
                if occupant > 1:
                    print(
                        f"{occupant_names} have been checked into Room: {room} on Floor: {floor}."
                    )
                else:
                    print(
                        f"{occupant_names} has been checked into Room: {room} on Floor: {floor}."
                    )
            else:
                print(f"Room: {room} is already occupied.")
        else:
            print("That room does not exist.")

    def remove_guest(self):
        floor, room = self.check_in_check_out()
        # Check if the floor and room the user provided is in the hotel
        if floor in self.hotel_data and room in self.hotel_data[floor]:
            # If the room is occupied check the user out
            if len(self.hotel_data[floor][room]) > 0:
                delete_guest = self.hotel_data[floor][room]
                self.hotel_data[floor][room] = []
                print(f"{", ".join(delete_guest)} has checked out.")
        else:
            print("That room does not exist.")

    def display_occupants_and_rooms(self):
        for floor in self.hotel_data:
            for room in self.hotel_data[floor]:
                guests = self.hotel_data[floor][room]
                print(f"Floors: {floor}, Rooms: {room}, Guests: {", ".join(guests)}")

    def guest_status_menu(self):
        tries = 3
        while tries > 0:
            self.welcome_message()

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


hollywood_hotel = Hotel("Hollywood Hotel")
hollywood_hotel.guest_status_menu()
