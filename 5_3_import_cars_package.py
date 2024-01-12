from cars.BMW import BMW  
from cars.AUDI import AUDI
from cars.NISSAN import  NISSAN  

bmw = BMW("M3", "blue") 
audi = AUDI("A5", 354)
nissan = NISSAN("Sentra", "hybrid")


bmw.start()
bmw.accelerate()
audi.drive()
nissan.brake()
