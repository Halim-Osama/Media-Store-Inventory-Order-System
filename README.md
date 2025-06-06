# 📚 Media Store Inventory & Order System

This Python project implements an **object-oriented system** for managing items (Books, Magazines, DVDs), inventory, and customer orders (online and in-store) using classes, inheritance, and abstraction.

---

## 🚀 Features

- Represent books, magazines, and DVDs using custom classes
- Manage items in an inventory
- Add, remove, and search items
- Create and manage customer orders
- Support both online and in-store order types
- Use inheritance and abstract classes to enforce design structure

---

## 🧱 Project Structure

### Core Classes

- **Item (Base Class)**: Represents a generic item with title, author, and price
- **Book / Magazine / DVD**: Specialized item types with additional attributes
- **Inventory**: Holds and manages all items in the store
- **Customer**: Stores customer details
- **Order (Abstract Class)**: Base class for all orders
- **OnlineOrder / InStoreOrder**: Represent customer orders placed online or in-store

---

## 📄 Example Usage

```python
book1 = Book("Python Programming", "John Doe", 29.99, "978-0-13-468747-9", "Programming", 400)
magazine1 = Magazine("Tech News", "Tech Insights", 9.99, 123, "April 2024", "Jane Smith")
dvd1 = DVD("The Matrix", "The Wachowskis", 14.99, "The Wachowskis", 136, "Science Fiction")

inventory = Inventory()
inventory.add_item(book1)
inventory.add_item(magazine1)
inventory.add_item(dvd1)
inventory.display_items()

customer = Customer("John Smith", "john@example.com")
online_order = OnlineOrder(customer, "123 Main Street, City")
online_order.add_item(book1)
online_order.display_order_details()
