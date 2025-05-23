class Bus:
    def __init__(self, number, route,total_seats):
        self.number=number
        self.route=route
        self.total_seats= total_seats
        self.booked_seats= 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        else:
            return False


class Passenger:
    def __init__(self, name,phone, bus):
        self.name=name
        self.phone= phone
        self.bus=bus


class Admin:
    def __init__(self,username='admin',password='1234'):
        self.username =username
        self.password = password

    def login(self, username,password):
        return self.username== username and self.password==password

class BusSystem:
    def __init__(self):
        self.buses= []
        self.passengers= []
        self.admin_logged_in= False
        self.admin =Admin()

    def add_bus(self, number,route, seats):
        for bus in self.buses:
            if bus.number== number:
                print("Bus with this number already exists")
                return
        new_bus= Bus(number,route,seats)
        self.buses.append(new_bus)
        print("Bus added successfully")

    def show_buses(self):
        if not self.buses:
            print("No buses available")
            return
        print("\nAvailable Buses:")
        for bus in self.buses:
            print(f"Bus No: {bus.number} Route: {bus.route} Seats Available: {bus.available_seats()}/{bus.total_seats}")
    

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number== number:
                return bus
        return None

    def book_ticket(self,number, name,phone):
        bus= self.find_bus(number)
        if not bus:
            print("Bus not found")
            return
        if bus.book_seat():
            passenger= Passenger(name,phone,bus)
            self.passengers.append(passenger)
            print(f"Ticket booked for {name} with Fare: ৳500")
        else:
            print("No seats available in this bus")

    def admin_menu(self):
        while True:
            print("\n---Admin Menu---")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            choice= input("Enter your choice: ")


            if choice== "1":
                number=input("Enter Bus Number: ")
                route=input("Enter Route: ")
                seats_input= input("Enter Total Seats: ")

                if not seats_input.isdigit():
                    print("Please enter a valid number for seats")
                    continue


                seats= int(seats_input)
                if seats <= 0:
                    print("Seats must be a positive number")
                    continue

                self.add_bus(number,route,seats)

            elif choice== "2":
                self.show_buses()
            elif choice== "3":
                self.admin_logged_in =False
                print("Admin logged out")
                break
            else:
                print("Invalid")

    def user_menu(self):
        while True:
            print("\n---Main Menu---")
            print("1. Admin Login")
            print("2. Book Ticket")
            print("3. View Buses")
            print("4. Exit")
            choice=input("Enter your choice: ")

            if choice== "1":
                username= input("Enter Admin Username: ")
                password= input("Enter Admin Password: ")
                if self.admin.login(username, password):
                    print("Login successful.")
                    self.admin_logged_in=True
                    self.admin_menu()
                else:
                    print("Invalid")
            elif choice== "2":
                if not self.buses:
                    print("No buses available to book")
                    continue
                number=input("Enter Bus Number: ")
                name= input("Enter Your Name: ")
                phone =input("Enter Your Phone Number: ")
                self.book_ticket(number,name, phone)
            elif choice =="3":
                self.show_buses()
            elif choice == "4":
                print("Thank you for using the Bus Ticket System")
                break
            else:
                print("Invalid option")

system= BusSystem()
system.user_menu()
