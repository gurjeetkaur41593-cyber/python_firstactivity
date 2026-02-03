import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

# ==========================================
# DATA LAYER (LO1: Testing & Procedures)
# ==========================================
class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect('car_rental_2025.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles 
                         (id INTEGER PRIMARY KEY, model TEXT, rate REAL, type TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS rentals 
                         (id INTEGER PRIMARY KEY, v_id INTEGER, days INTEGER, total REAL, date TEXT)''')
        self.conn.commit()

# ==========================================
# LOGIC LAYER (LO2: Innovative Solutions)
# ==========================================
class Vehicle(ABC):
    """Abstraction: Abstract base class for all vehicle types."""
    def __init__(self, v_id, model, base_rate):
        self._v_id = v_id  # Encapsulation
        self.model = model
        self.base_rate = base_rate

    @abstractmethod
    def calculate_fare(self, days):
        pass

class EconomyCar(Vehicle):
    """Inheritance & Polymorphism: Specific fare logic for economy."""
    def calculate_fare(self, days):
        return self.base_rate * days

class PremiumCar(Vehicle):
    """Inheritance & Polymorphism: Includes 15% luxury tax."""
    def calculate_fare(self, days):
        return (self.base_rate * days) * 1.15

# ==========================================
# MANAGEMENT LAYER (GPO4: Problem Solving)
# ==========================================
class RentalSystem:
    def __init__(self, db):
        self.db = db

    def process_rental(self, vehicle, days):
        try:
            total = vehicle.calculate_fare(days)
            cursor = self.db.conn.cursor()
            cursor.execute("INSERT INTO rentals (v_id, days, total, date) VALUES (?, ?, ?, ?)",
                           (vehicle._v_id, days, total, datetime.now().strftime("%Y-%m-%d")))
            self.db.conn.commit()
            print(f"SUCCESS: {vehicle.model} rented for {days} days. Total: ${total:.2f}")
        except Exception as e:
            print(f"CRITICAL ERROR: {e}")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    db_handler = DatabaseHandler()
    system = RentalSystem(db_handler)

    # Creating Objects
    car1 = EconomyCar(101, "Toyota Corolla", 50.0)
    car2 = PremiumCar(202, "BMW M4", 150.0)

    # Simulating Business Use Case
    print("--- 2025 Car Rental System Initialized ---")
    system.process_rental(car1, 5)  # Standard pricing
    system.process_rental(car2, 3)  # Premium pricing applied
