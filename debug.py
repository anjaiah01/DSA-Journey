class Car:
    def start(self):
        print("Start the Car")
        
def newStart(self):
    print("New Method replaced using monkey patching")
    
Car.start = newStart  # new method replaced using the money patching

mp=Car()
mp.start()