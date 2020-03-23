'''
' Tester code for lab 01.
'''

from Vehicle import Vehicle
from Bicycle import Bicycle
from MotorVehicle import MotorVehicle

#I) Try to construct the Vehicle which should fail
print("I) Try to construct the Vehicle which should fail")
try:
    v1 = Vehicle(10, 25, (0,0), "NORTH")
    print("Vehcile is not abstract.")
except:
    print("GOOD NEWS! Vehicle is abstract!")
finally:
    print("--------------------------------")

#II) Test the inherited accessor methods of Vehicle in Bicycle
print("\nII) Test the inherited accessor methods of Vehicle in Bicycle")
v1 = Bicycle(25, (5,-3), "SOUTH")
print("5       = " + str(v1.get_length()))
print("25      = " + str(v1.get_top_speed()))
print("SOUTH   = " + str(v1.get_direction()))
print("(5,-3)  = " + str(v1.get_location()))
print("0       = " + str(v1.get_current_speed()))

#III) Test the inherited turn_left method of Vehicle in Bicycle
print("\nIII) Test the inherited turn_left method of Vehicle in Bicycle")
v1.turn_left()
print("EAST    = " + v1.get_direction())
v1.turn_left()
print("NORTH   = " + v1.get_direction())
v1.turn_left()
print("WEST    = " + v1.get_direction())
v1.turn_left()
print("SOUTH   = " + v1.get_direction())

#IV) Test the inherited turn_right method of Vehicle in Bicycle
print("\nIV) Test the inherited turn_right method of Vehicle in Bicycle")
v1.turn_right()
print("WEST    = " + v1.get_direction())
v1.turn_right()
print("NORTH   = " + v1.get_direction())
v1.turn_right()
print("EAST    = " + v1.get_direction())
v1.turn_right()
print("SOUTH   = " + v1.get_direction())

#V) Test the accelerate and decelerate methods in Bicycle
print("\nV) Test the accelerate and decelerate methods in Bicycle")
v1.accelerate()
print(str(v1.get_top_speed()) + "      = " + str(v1.get_current_speed()))
v1.accelerate()
print(str(v1.get_top_speed()) + "      = " + str(v1.get_current_speed()))
v1.decelerate()
print("0       = " + str(v1.get_current_speed()))
v1.decelerate()
print("0       = " + str(v1.get_current_speed()))

#VI) Test the inherited move method in Bicycle
print("\nVI) Test the inherited move method in Bicycle")
v1.move()
print("(5,-3)  = " + str(v1.get_location()))
v1.accelerate()
v1.move()
print("(5,-28) = " + str(v1.get_location()))
v1.decelerate()
v1.turn_left()
v1.move()
print("(5,-28) = " + str(v1.get_location()))
v1.accelerate()
v1.turn_left()
v1.move()
print("(5,-3)  = " + str(v1.get_location()))
v1.turn_right()
v1.move()
print("(30,-3) = " + str(v1.get_location()))
print("--------------------------------")

#VII) Test the inherited accessor methods of Vehicle in MotorVehicle
print("\nVII) Test the inherited accessor methods of Vehicle in MotorVehicle")
v1 = MotorVehicle(13, 25, (5,-3), "SOUTH", "PLATE123", 0.2)
print("13      = " + str(v1.get_length()))
print("25      = " + str(v1.get_top_speed()))
print("SOUTH   = " + str(v1.get_direction()))
print("(5,-3)  = " + str(v1.get_location()))
print("0       = " + str(v1.get_current_speed()))

#VIII) Test the newly declared methods in MotorVehicle
print("\nVIII) Test the newly declared methods in MotorVehicle")
print("0.2     = " + str(v1.get_acceleration()))
print("PLATE123= " + str(v1.get_license_plate()))
v1.set_license_plate("HEY987")
print("HEY987  = " + str(v1.get_license_plate()))

#IX) Test the accelerate method in MotorVehicle
print("\nIX) Test the accelerate method in MotorVehicle")
v1.accelerate()
print("5       = " + str(v1.get_current_speed()))
v1.accelerate()
print("10      = " + str(v1.get_current_speed()))
v1.accelerate()
print("15      = " + str(v1.get_current_speed()))
v1.accelerate()
print("20      = " + str(v1.get_current_speed()))
v1.accelerate()
print("25      = " + str(v1.get_current_speed()))
v1.accelerate()
print("25      = " + str(v1.get_current_speed()))

#X) Test the decelerate method in Bicycle
print("\nX) Test the decelerate method in Bicycle")
v1.decelerate()
print("20      = " + str(v1.get_current_speed()))
v1.decelerate()
print("15      = " + str(v1.get_current_speed()))
v1.decelerate()
print("10      = " + str(v1.get_current_speed()))
v1.decelerate()
print("5       = " + str(v1.get_current_speed()))
v1.decelerate()
print("0       = " + str(v1.get_current_speed()))
v1.decelerate()
print("0       = " + str(v1.get_current_speed()))

#XI) Test the overridden turn_left method of Vehicle in MotorVehicle
print("\nXI) Test the overridden turn_left method of Vehicle in MotorVehicle")
v1.accelerate()
v1.accelerate()
v1.accelerate()
v1.accelerate()
v1.accelerate()
v1.turn_left()
print("EAST    = " + v1.get_direction())
print("20      = " + str(v1.get_current_speed()))
v1.turn_left()
print("NORTH   = " + v1.get_direction())
print("15      = " + str(v1.get_current_speed()))
v1.turn_left()
print("WEST    = " + v1.get_direction())
print("10      = " + str(v1.get_current_speed()))
v1.turn_left()
print("SOUTH   = " + v1.get_direction())
print("5       = " + str(v1.get_current_speed()))

#XII) Test the overridden turn_right method of Vehicle in MotorVehicle
print("\nXII) Test the overridden turn_right method of Vehicle in MotorVehicle")
v1.accelerate()
v1.accelerate()
v1.accelerate()
v1.accelerate()
v1.turn_right()
print("WEST    = " + v1.get_direction())
print("20      = " + str(v1.get_current_speed()))
v1.turn_right()
print("NORTH   = " + v1.get_direction())
print("15      = " + str(v1.get_current_speed()))
v1.turn_right()
print("EAST    = " + v1.get_direction())
print("10      = " + str(v1.get_current_speed()))
v1.turn_right()
print("SOUTH   = " + v1.get_direction())
print("5       = " + str(v1.get_current_speed()))

#XIII) Test the inherited move method in MotorVehicle
print("\nXIII) Test the inherited move method in MotorVehicle")
v1.move()
print("(5,-8)  = " + str(v1.get_location()))
v1.accelerate()
v1.move()
print("(5,-18) = " + str(v1.get_location()))
v1.turn_left()
v1.move()
print("(10,-18)= " + str(v1.get_location()))
v1.accelerate()
v1.turn_left()
v1.move()
print("(10,-13)= " + str(v1.get_location()))
v1.turn_right()
v1.move()
print("(10,-13)= " + str(v1.get_location()))

