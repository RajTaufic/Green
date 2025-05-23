def main():
    system = BusSystem()

    while True:
        print("\n--- Main Menu ---")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Admin Username: ")
            password = input("Admin Password: ")
            if system.admin.login(username, password):
                print("Admin login successful.")
                system.logged_in = True

                while system.logged_in:
                    print("\n--- Admin Menu ---")
                    print("1. Add Bus")
                    print("2. View All Buses")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        number = input("Enter Bus Number: ")
                        route = input("Enter Route: ")
                        try:
                            seats = int(input("Enter Total Seats: "))
                            system.add_bus(number, route, seats)
                        except ValueError:
                            print("Invalid seat number")
                    elif admin_choice == "2":
                        system.show_buses()
                    elif admin_choice == "3":
                        system.logged_in = False
                        print("Logged out")
                    else:
                        print("Invalid choice")

            else:
                print("Login failed. Try again")

        elif choice == "2":
            number = input("Enter Bus Number: ")
            name = input("Enter Your Name: ")
            phone = input("Enter Phone Number: ")
            system.book_ticket(number, name, phone)

        elif choice == "3":
            system.show_buses()

        elif choice == "4":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid input. Please choose from 1-4.")
