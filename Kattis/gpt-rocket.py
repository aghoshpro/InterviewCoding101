# Import necessary modules
import math
import time

# Define constants
GRAVITY = 9.8  # acceleration due to gravity (m/s^2)
THRUST = 1000  # thrust of the rocket engines (N)
MASS = 10000  # mass of the rocket (kg)
DRAG = 100  # drag coefficient of the rocket

# Define initial conditions
altitude = 100000  # initial altitude of the rocket (m)
velocity = 0  # initial velocity of the rocket (m/s)

# Define time step
dt = 0.1  # time step (s)

# Define a function to calculate the acceleration of the rocket
def calc_acceleration(altitude, velocity):
  # Calculate the force of gravity
  force_gravity = GRAVITY * MASS
  
  # Calculate the force of drag
  force_drag = 0.5 * DRAG * velocity**2
  
  # Calculate the total force acting on the rocket
  force_total = force_gravity + force_drag
  
  # Calculate the acceleration of the rocket
  acceleration = force_total / MASS
  
  return acceleration

# Define a function to calculate the new altitude and velocity of the rocket
def update_position(altitude, velocity, acceleration, dt):
  # Calculate the new altitude of the rocket
  new_altitude = altitude + velocity * dt + 0.5 * acceleration * dt**2
  
  # Calculate the new velocity of the rocket
  new_velocity = velocity + acceleration * dt
  
  return new_altitude, new_velocity

# Define a function to land the rocket
def land_rocket(altitude, velocity):
  # Set the initial thrust of the rocket engines
  thrust = THRUST
  
  # Print the initial conditions
  print(f"Altitude: {altitude:.2f} m")
  print(f"Velocity: {velocity:.2f} m/s")
  
  # Loop until the rocket reaches the ground
  while altitude > 0:
    # Calculate the acceleration of the rocket
    acceleration = calc_acceleration(altitude, velocity)
    
    # Update the altitude and velocity of the rocket
    altitude, velocity = update_position(altitude, velocity, acceleration, dt)
    
    # If the rocket is descending too quickly, reduce the thrust
    if velocity > 20:
      thrust = 500
    elif velocity > 10:
      thrust = 750
    else:
      thrust = THRUST
    
    # Print the current conditions
    print(f"Altitude: {altitude:.2f} m")
    print(f"Velocity: {velocity:.2f} m/s")
    print(f"Thrust: {thrust:.2f} N")
    
    # Pause for 0.1 seconds
    time.sleep(dt)

# Call the land_rocket function to land the rocket
land_rocket(altitude, velocity)
