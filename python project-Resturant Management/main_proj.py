from food_item import FoodItem
from menu import Menu
from users import customer, Admin, Employee
from restaurent import Restaurant
from orders import Order

mamar_restaurent = Restaurant('mamar restaurent')

def customer_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')

    Customer = customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'\nWelcome {Customer.name}!!!')
        print('1. View menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. Pay bill')
        print('5. Exit')

        choice = int(input('Enter your input: '))
        if choice == 1:
            Customer.view_menu(mamar_restaurent)

        elif choice == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            Customer.add_to_cart(mamar_restaurent, item_name, item_quantity)

        elif choice == 3:
            Customer.view_cart()

        elif choice == 4:
            Customer.pay_bill()

        elif choice == 5:
            break
        else:
            print('Invalid Input')

def admin_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'\nWelcome {admin.name}!!!')
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Employee')
        print('4. View Items')
        print('5. Delete Item')
        print('6. Exit')

        choice = int(input('Enter your input: '))
        if choice == 1:
            item_name = input('Enter Item Name: ')
            item_price = int(input('Enter Item Price: '))
            item_quantity = int(input('Enter Item Quantity: '))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)

        elif choice == 2:
            name = input('Enter employee name: ')
            phone = input('Enter employee phone: ')
            email = input('Enter employee email: ')
            designation = input('Enter employee designation: ')
            age = input('Enter employee age: ')
            salary = input('Enter employee salary: ')
            address = input('Enter employee address: ')
            admin.add_employee(name, phone, email, address, age, designation, salary)

        elif choice == 3:
            admin.view_employee(mamar_restaurent)

        elif choice == 4:
            admin.view_menu(mamar_restaurent)

        elif choice == 5:
            item_name = input('Enter Item Name to remove: ')
            admin.remove_items(mamar_restaurent, item_name)

        elif choice == 6:
            break
        else:
            print('Invalid Input')

# Main program
while True:
    print('\nWelcome !!!')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print('Invalid Input !!')
