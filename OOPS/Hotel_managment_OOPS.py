class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def contact_info(self):
        print(f"{self.name} : {self.phone}")

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}"  


class Guest(Person):
    def __init__(self, name, age, phone, guest_id, nationality):
        super().__init__(name, age, phone)
        self.guest_id = guest_id
        self.nationality = nationality

    def __str__(self):
        base = super().__str__()
        return f"{base} | Guest ID: {self.guest_id} | Nationality: {self.nationality}"


class Staff(Person):
    def __init__(self, name, age, phone, role, salary):
        super().__init__(name, age, phone)
        self.role = role
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        base = super().__str__()
        return f"{base} | Role: {self.role} | Salary: ₹{self.salary}"


class Room:
    def __init__(self, room_no, room_type, price_per_night, is_available=True):
        self.room_no = room_no
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available

    def book_room(self):                    
        self.is_available = False

    def vacate_room(self):
        self.is_available = True

    def __str__(self):
        return (f"Room {self.room_no} | {self.room_type} | "
                f"₹{self.price_per_night}/night | Available: {self.is_available}")


class Hotel:
    total_hotels = 0

    def __init__(self, hotel_name):
        self.name = hotel_name
        self.rooms = []
        self.guests = []
        self.staff = []
        Hotel.total_hotels += 1

    def add_room(self, room):
        self.rooms.append(room)

    def hire_staff(self, staff):
        self.staff.append(staff)

    def check_in(self, guest, room_no):
        for room in self.rooms:
            if room.room_no == room_no:              
                if room.is_available:
                    room.book_room()
                    self.guests.append(guest)
                    print(f"{guest.name} checked into Room {room_no}.")
                else:
                    print(f"Room {room_no} is not available.")
                return
        print(f"Room {room_no} not found.")

    def check_out(self, guest_name, room_no):
        for guest in self.guests:
            if guest.name == guest_name:             
                self.guests.remove(guest)
                for room in self.rooms:
                    if room.room_no == room_no:
                        room.vacate_room()           
                        print(f"{guest_name} checked out of Room {room_no}.")
                return
        print(f"Guest '{guest_name}' not found.")

    def available_rooms(self):
        print("\n-- Available Rooms --")
        for room in self.rooms:
            if room.is_available:                    
                print(room)

    def show_staff(self):
        print("\n-- Hotel Staff --")
        for s in self.staff:
            print(s)

    def find_guest(self, name):
        for guest in self.guests:
            if guest.name == name:                  
                return guest
        print(f"Guest '{name}' not found.")
        return None

    def __str__(self):
        return (f"Hotel: {self.name} | "
                f"Rooms: {len(self.rooms)} | "
                f"Guests checked in: {len(self.guests)}")


h1 = Hotel("Taj Hotels")

# Rooms
r1 = Room(101, "Deluxe", 5000)
r2 = Room(102, "Suite", 12000)
r3 = Room(103, "Standard", 2500)

# Staff
s1 = Staff("Ramesh", 35, "9111111111", "Manager", 75000)
s2 = Staff("Priya", 28, "9222222222", "Receptionist", 35000)

# Guests
g1 = Guest("Abhay", 19, "9999999999", "G001", "Indian")
g2 = Guest("Yash", 20, "8888888888", "G002", "Indian")
g3 = Guest("James", 30, "7777777777", "G003", "British")

# Add to hotel
h1.add_room(r1)
h1.add_room(r2)
h1.add_room(r3)
h1.hire_staff(s1)
h1.hire_staff(s2)

# Check in
h1.check_in(g1, 101)
h1.check_in(g2, 102)
h1.check_in(g3, 103)

# Display
print(h1)
h1.available_rooms()
h1.show_staff()

# Check out
h1.check_out("Abhay", 101)
h1.available_rooms()

# Search
found = h1.find_guest("James")
print(found)
h1.find_guest("Ronaldo")

# Property
print(s1.salary)

# Contact
g1.contact_info()
s1.contact_info()

# Class variable
h2 = Hotel("Oberoi Hotels")
print(Hotel.total_hotels)   # should print 2