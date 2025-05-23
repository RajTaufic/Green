from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):  
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.item_show()  # Fix here: item_show()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('item quantity exceeded')
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print('item added')
        else:
            print('Item not found')

    def view_cart(self):
        print('***View Cart***')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price: {self.cart.total_price}')

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_items(item)

    def remove_items(self, restaurant, item_name):
        restaurant.menu.remove_items(item_name)



# Example usage
res = Restaurant('Mamar Restaurant') 

item1 = FoodItem('Burger', 85.5, 5)
item2 = FoodItem('Pizza', 800.5, 8)
admin = Admin('Ramim','ramim@gmail.com',8907,'Gulshan')
admin.add_new_item(res, item1)
admin.add_new_item(res, item2)

customer1 = Customer('Rifat', 9012, 'rifat@gmail.com', 'Banani')
customer1.view_menu(res)

# # Customer adding items
# customer1.add_to_cart(res, 'Burger', 2)
# customer1.add_to_cart(res, 'Pizza', 1)
item_name=input('Enter your item : ')
item_quantity=int(input('Enter item quantity : '))

customer1.add_to_cart(res,item_name,item_quantity)
customer1.view_cart()

