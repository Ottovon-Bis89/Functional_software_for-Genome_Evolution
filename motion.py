"""
This Python script simulates the motion of a projectile under the influence of gravity. The simulation is based on the kinematic equations of projectile motion and uses the Numpy library.

The script defines a function called 'projectile_motion' that takes in the initial velocity, angle, time step, and total time as input variables. The function calculates and returns the values of the horizontal position (x), vertical position (y), time (t), horizontal velocity (vx), and vertical velocity (vy) of the projectile at each time step.

The script also plots graphs of the horizontal position vs. time and the vertical position vs. time.

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(initial_velocity, angle, time_step, total_time):
    # Convert the angle from degrees to radians
    theta = np.radians(angle)
    
    # Initialize the x, y, t, vx, and vy arrays
    x = np.zeros(int(total_time / time_step) + 1)
    y = np.zeros(int(total_time / time_step) + 1)
    t = np.zeros(int(total_time / time_step) + 1)
    vx = np.zeros(int(total_time / time_step) + 1)
    vy = np.zeros(int(total_time / time_step) + 1)
    
    # Set the initial values
    x[0] = 0
    y[0] = 0
    t[0] = 0
    vx[0] = initial_velocity * np.cos(theta)
    vy[0] = initial_velocity * np.sin(theta)    
    
    # Calculate the values at each time step
    for i in range(1, len(t)):
        t[i] = t[i-1] + time_step
        x[i] = x[i-1] + vx[i-1] * time_step
        y[i] = y[i-1] + vy[i-1] * time_step - 0.5 * 9.81 * time_step**2
        vx[i] = vx[i-1]
        vy[i] = vy[i-1] - 9.81 * time_step
    
    return x, y, t, vx, vy

# Set the input values
initial_velocity = 10
angle = 45
time_step = 0.01
total_time = 2

# Call the function to calculate the projectile motion
x, y, t, vx, vy = projectile_motion(initial_velocity, angle, time_step, total_time)

# Plot the horizontal position vs. time
plt.plot(t, x)
plt.title('Horizontal Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Horizontal Position (m)')
plt.show()

# Plot the vertical position vs. time
plt.plot(t, y)
plt.title('Vertical Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Vertical Position (m)')
plt.show()

