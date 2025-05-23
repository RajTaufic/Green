class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()
        self.logged_in = False

    def add_bus(self, number, route, total_seats):
        if self.logged_in:
            bus = Bus(number, route, total_seats)
            self.buses.append(bus)
            print("Bus added successfully")
        else:
            print("Only admin can add buses")

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None

    def book_ticket(self, number, name, phone):
        bus = self.find_bus(number)
        if bus:
            if bus.book_seat():
                passenger = Passenger(name, phone, bus)
                self.passengers.append(passenger)
                print(f"Ticket booked for {name}. Fare: ৳500")
            else:
                print("No seats available")
        else:
            print("Bus not found")

    def show_buses(self):
        if not self.buses:
            print("No buses available")
        for bus in self.buses:
            print(f"Bus No: {bus.number} | Route: {bus.route} | Available Seats: {bus.available_seats()}")
