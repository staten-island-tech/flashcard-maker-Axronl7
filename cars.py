import json
try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []
class Car:
    def __init__(self, make, model, year, image_path=None):
        self.make = make
        self.model = model
        self.year = year
        self.image_path = image_path
    
    def display_info(self):
        return f"{self.year}  {self.model}"
    
    def show_image(self):
        if self.image_path:
            try:
                img = Image.open(self.image_path)
                img.show()
            except FileNotFoundError:
                print("Error: Image file not found.")
        else:
            print("No image provided.")


cars = [
    Car("Toyota", "Camry", 2023, "car1.avif"),
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

""" # Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4) """
new_car = Car("Chevrolet", "Malibu", 2024, "car1.jpg")
new_car.show_image()
# Append new car
cars_data.append(new_car.__dict__)

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)