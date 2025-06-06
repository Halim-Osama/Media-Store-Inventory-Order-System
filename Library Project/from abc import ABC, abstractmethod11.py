from abc import ABC, abstractmethod

class Item:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    def get_details(self):
        return f"Title: {self._title}, Author: {self._author}, Price: ${self._price}"

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_price(self):
        return self._price
    
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author
        
    def set_price(self, price):
        self._price = price

class Book(Item):
    def __init__(self, title, author, price, isbn, genre, num_pages):
        super().__init__(title, author, price)
        self.isbn = isbn
        self.genre = genre
        self.num_pages = num_pages

    def get_details(self):
        item_details = super().get_details()
        return f"{item_details}, ISBN: {self.isbn}, Genre: {self.genre}, Pages: {self.num_pages}"

    def get_isbn(self):
        return self.isbn

    def get_genre(self):
        return self.genre

    def get_num_pages(self):
        return self.num_pages


class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self.issue_number = issue_number
        self.publication_date = publication_date
        self.editor = editor

    def get_details(self):
        item_details = super().get_details()
        return f"{item_details}, Issue: {self.issue_number}, Published: {self.publication_date}, Editor: {self.editor}"

    def get_issue_number(self):
        return self.issue_number

    def get_publication_date(self):
        return self.publication_date

    def get_editor(self):
        return self.editor


class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre

    def get_details(self):
        item_details = super().get_details()
        return f"{item_details}, Director: {self.director}, Duration: {self.duration} mins, Genre: {self.genre}"

    def get_director(self):
        return self.director

    def get_duration(self):
        return self.duration

    def get_genre(self):
        return self.genre


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_items(self):
        for item in self.items:
            print(item.get_details())

    def search_by_title(self, title):
        results = [item for item in self.items if item.get_title() == title]
        for i in results:
           item= results[i]
           print(item.get_details())

    def search_by_author(self, author):
        results = [item for item in self.items if item.get_author() == author]
        for i in results:
           item= results[i]
           print(item.get_details())

    def search_by_genre(self, genre):
        results = [item for item in self.items if hasattr(item, 'genre') and item.get_genre() == genre]
        for i in results:
           item= results[i]
           print(item.get_details())


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email


class Order(ABC):
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_customer(self):
        return self.customer

    def get_total(self):
        return sum(item.get_price() for item in self.items)

    @abstractmethod
    def display_order_details(self):
        pass


class OnlineOrder(Order):
    def __init__(self, customer, shipping_address):
        super().__init__(customer)
        self.shipping_address = shipping_address

    def set_shipping_address(self, shipping_address):
        self.shipping_address = shipping_address

    def get_shipping_address(self):
        return self.shipping_address

    def display_order_details(self):
        print("Online Order Details:")
        print(f"Customer: {self.customer.get_name()}")
        print(f"Shipping Address: {self.shipping_address}")
        print("Items:")
        for item in self.items:
            print(item.get_details())
        print(f"Total: ${self.get_total()}")


class InStoreOrder(Order):
    def __init__(self, customer, store_location):
        super().__init__(customer)
        self.store_location = store_location

    def set_store_location(self, store_location):
        self.store_location = store_location

    def get_store_location(self):
        return self.store_location

    def display_order_details(self):
        print("In-Store Order Details:")
        print(f"Customer: {self.customer.get_name()}")
        print(f"Store Location:{self.store_location}")
        print("Items:")
        for item in self.items:
            print(item.get_details())
        print(f"Total: ${self.get_total()}")


# Example usage
book1 = Book("Python Programming", "John Doe", 29.99, "978-0-13-468747-9", "Programming", 400)
magazine1 = Magazine("Tech News", "Tech Insights", 9.99, 123, "April 2024", "Jane Smith")
dvd1 = DVD("The Matrix", "The Wachowskis", 14.99, "The Wachowskis", 136, "Science Fiction")

inventory = Inventory()
inventory.add_item(book1)
inventory.add_item(magazine1)
inventory.add_item(dvd1)
inventory.display_items()
book1.set_price(350)
print(book1.get_details())

customer = Customer("John Smith", "john@example.com")
online_order = OnlineOrder(customer, "123 Main Street, City")
online_order.add_item(book1)
online_order.add_item(magazine1)
online_order.display_order_details()
instore_order = InStoreOrder(customer, "City Center Store")
instore_order.add_item(dvd1)
instore_order.display_order_details()