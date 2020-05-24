# Cars

## Overview

Cars is an object-oriented script written in Python 3.x that lets the user create a car with specified brand, engine type (gasoline or Diesel), tank capacity and tanked fuel.

## Class parameters
* brand (string)- name of a brand of a car

* engine_type (int(0,1))- type of engine, 1 for gasoline, 0 for Diesel

* tank_capacity (int) - capacity of car's tank

* tanked_fuel (int) - amount of fuel in car's tank


## Class methods
* fill_tank - filling tank of specified car, without parameter fills tank to maximum, with parameter fills tank with specified liters
* empty_tank - empties tank to centrain percentage, returns amount of lost liters. 

## Usage

To use this script simply import this to Python interpreter

      import cars

To create a new car:

      cars.Car(brand, tank_capacity, tanked_fuel, engine_type)

To fill tank of created car to full:

      car.fill_tank()
      
To fill tank of created car for specified liters:

      car.fill_tank(liters)

To empty tank to centrain percentage (limit):

      car.empty_tank(limit)
      
## Exceptions

If car has diesel engine type then in case of calling fill_tank method it will raise an EnvironmentalError exception. 

    >>> car = cars.Cars("Audi", 150, 100, 0)
    >>> car.fill_tank()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/daria/.virtualenvs/zadanie/cars.py", line 22, in fill_tank
      raise EnvironmentalError("ON fuel not available,because of environmental restrictions. Change engine as soon, as possible.")
    cars.EnvironmentalError: ON fuel not available,because of environmental restrictions. Change engine as soon, as possible.

If user is trying to create a car with fuel amount above tanked capacity then the constructor will raise a ValueError exception.

    >>> car = cars.Cars("Audi", 100, 150, 1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/daria/.virtualenvs/zadanie/cars.py", line 13, in __init__
    raise ValueError("You cannot create car with fuel amount above its' tank capacity")
    ValueError: You cannot create car with fuel amount above its' tank capacity



If user is trying to use fill_tank method with liters exceeding tank capacity then fill_tank method will raise ValueError exception.
    
    >>> car.fill_tank(70)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/daria/.virtualenvs/zadanie/cars/cars/cars.py", line 26, in fill_tank
        raise ValueError("You cannot fill tank over its capacity!")
    ValueError: You cannot fill tank over its capacity!

## Contributors
Daria Ostapczuk @dostapczuk 
