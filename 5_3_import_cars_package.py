from cars.BMW import BMW  # Import the BMW class from the cars.BMW module
from cars.AUDI import AUDI  # Import the AUDI class from the cars.AUDI module
from cars.NISSAN import NISSAN  # Import the NISSAN class from the cars.NISSAN module

# Create objects of each car class
bmw = BMW("M3", "blue")  # Create a BMW object with model "M3" and color "blue"
audi = AUDI("A5", 354)   # Create an AUDI object with model "A5" and horsepower 354
nissan = NISSAN("Sentra", "hybrid")  # Create a NISSAN object with model "Sentra" and engine type "hybrid"

# Call methods on the car objects
bmw.start()  # Start the BMW
bmw.accelerate()  # Accelerate the BMW
audi.drive()   # Drive the AUDI
nissan.brake()  # Brake the NISSAN
