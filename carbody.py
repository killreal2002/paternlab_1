from carparts import *

class Car():
    '''
    A class to represent a car
    ...
    Attributes
    ---------
    registration : str
      registration date
    year : int
      year of production
    licenseNumber: str
      licenseNumber
    carmodel
    engine
    gearbox
    body
    suspension
    brake
    '''
    def __init__(self, registration : str, year : int, licenseNumber: str, carmodel, engine, gearbox, body,
                 suspension, brake):
        self.registration = registration
        self.year = year
        self.licenceNumber = licenseNumber
        self.carmodel = carmodel
        self.engine = engine
        self.gearbox = gearbox
        self.body = body
        self.suspension = suspension
        self.brake = brake
        '''
        Method that construct all the necessary atributes for the car object 
        '''

    def moveForward(self):
        print("Moving forward")
    def moveBackward(self):
        print("Moving backward")
    def stop(self):
        print("The car has stopped")
    def turnRight(self):
        print("turning right")
    def turnLeft(self):
        print("turning left")
        '''
        These are all methods that simulates car object moves 
        '''