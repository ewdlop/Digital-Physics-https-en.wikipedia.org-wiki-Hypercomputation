import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def compute_worldline_observer(t):
    """
    Compute the worldline of an observer in Malament-Hogarth spacetime.
    Using a simple radial trajectory.
    """
    # Initial conditions
    r0 = 10.0  # Starting radius
    
    # Radial position over time
    r = r0 * np.exp(-t/10)
    
    return r

def compute_worldline_computer(t):
    """
    Compute the worldline of the computing system in M-H spacetime.
    Using a trajectory that approaches the singularity.
    """
    # Initial conditions
    r0 = 8.0  # Starting radius
    
    # Radial position over time
    r = r0 * (1 - t/100)
    
    return r

# Time points for simulation
t = np.linspace(0, 80, 1000)

# Compute worldlines
r_observer = compute_worldline_observer(t)
r_computer = compute_worldline_computer(t)

# Create the plot
plt.figure(figsize=(10, 8))
plt.plot(t, r_observer, 'b-', label='Observer Worldline')
plt.plot(t, r_computer, 'r--', label='Computer Worldline')

# Add singularity line
plt.axhline(y=0, color='k', linestyle=':')

# Customize the plot
plt.xlabel('Proper Time τ')
plt.ylabel('Radial Coordinate r')
plt.title('Worldlines in Malament-Hogarth Spacetime')
plt.legend()
plt.grid(True)

# Add annotations
plt.annotate('Singularity', xy=(40, 0.2), xytext=(45, 2),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Observer reaches infinity\nin finite proper time', 
            xy=(70, r_observer[-1]), xytext=(50, 6),
            arrowprops=dict(facecolor='blue', shrink=0.05))

# Calculate accumulation point
t_accum = 100  # Time when computer reaches singularity
r_accum = 0    # Radial coordinate at singularity

plt.annotate('Accumulation Point', xy=(t_accum, r_accum), 
            xytext=(70, 1),
            arrowprops=dict(facecolor='red', shrink=0.05))

plt.ylim(-0.5, 12)
plt.show()

# Calculate some interesting quantities
infinite_time_ratio = t[-1] / t[0]
print(f"Ratio of final to initial proper time: {infinite_time_ratio:.2f}")

separation = np.abs(r_observer - r_computer)
max_separation = np.max(separation)
print(f"Maximum spatial separation between worldlines: {max_separation:.2f}")

# Estimate proper time remaining for observer
remaining_time = 10 * np.log(r_observer[-1])  # Based on exponential decay
print(f"Estimated proper time remaining for observer: {remaining_time:.2f}")
