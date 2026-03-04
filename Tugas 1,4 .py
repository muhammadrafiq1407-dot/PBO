class Vehicle:
    def __init__(self, brand, model):
        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError("Brand dan model harus string!")
        if not brand or not model:
            raise ValueError("Brand dan model tidak boleh kosong!")
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        try:
            doors = int(doors)
        except (ValueError, TypeError):
            raise TypeError("Doors harus angka!")
        
        if doors <= 0:
            raise ValueError("Doors harus lebih dari 0!")
        if doors > 10:
            raise ValueError("Doors maksimal 10!")
        
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        try:
            load_capacity = int(load_capacity)
        except (ValueError, TypeError):
            raise TypeError("Load capacity harus angka!")
        
        if load_capacity <= 0:
            raise ValueError("Load capacity harus lebih dari 0!")
        
        self.load_capacity = load_capacity
        self.current_load = 0
    
    def load(self, weight):
        try:
            weight = float(weight)
        except (ValueError, TypeError):
            raise TypeError("Weight harus angka!")
        
        if weight <= 0:
            raise ValueError("Weight harus lebih dari 0!")
        
        if self.current_load + weight > self.load_capacity:
            raise ValueError(f"Melebihi kapasitas! Max: {self.load_capacity} kg")
        
        self.current_load += weight
        print(f"Loaded {weight} kg. Total: {self.current_load}/{self.load_capacity} kg")

def main():
    """Function utama untuk testing"""
    
    
    my_car = Car("Toyota","Avanza", 4)
    
    
    my_truck = Truck("Ford", "F-150", 1000)
    
    
    my_car.drive()
    my_car.honk()
    
    
    my_truck.drive()
    my_truck.load(1200)


if __name__ == "__main__":
    main()