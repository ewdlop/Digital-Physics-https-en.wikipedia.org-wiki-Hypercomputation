import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class WaterProperties:
    specific_heat: float = 4.186  # kJ/kg·K
    latent_heat_vaporization: float = 2260  # kJ/kg
    initial_temperature: float = 20  # °C
    boiling_point: float = 100  # °C

class NuclearPhysicsCalculator:
    def __init__(self):
        self.water = WaterProperties()
        
    def calculate_water_temperature_rise(self, energy_joules, mass_kg):
        """
        Calculate temperature rise in water from energy absorption
        Returns: final temp and state changes
        """
        # Convert joules to kilojoules
        energy_kj = energy_joules / 1000
        
        # Energy needed to reach boiling
        energy_to_boiling = mass_kg * self.water.specific_heat * \
            (self.water.boiling_point - self.water.initial_temperature)
        
        # If not enough energy to reach boiling
        if energy_kj < energy_to_boiling:
            delta_t = energy_kj / (mass_kg * self.water.specific_heat)
            final_temp = self.water.initial_temperature + delta_t
            return {
                'final_temperature': final_temp,
                'phase': 'liquid',
                'energy_absorbed': energy_kj
            }
        
        # Energy needed to vaporize
        energy_to_vaporize = mass_kg * self.water.latent_heat_vaporization
        remaining_energy = energy_kj - energy_to_boiling
        
        # If water vaporizes
        if remaining_energy >= energy_to_vaporize:
            # Calculate superheated steam temperature
            remaining_energy = remaining_energy - energy_to_vaporize
            delta_t_steam = remaining_energy / (mass_kg * 2.08)  # Steam specific heat
            final_temp = self.water.boiling_point + delta_t_steam
            return {
                'final_temperature': final_temp,
                'phase': 'superheated_steam',
                'energy_absorbed': energy_kj
            }
        
        # Partially vaporized
        return {
            'final_temperature': self.water.boiling_point,
            'phase': 'mixed',
            'vapor_fraction': remaining_energy / energy_to_vaporize,
            'energy_absorbed': energy_kj
        }

    @staticmethod
    def calculate_radiation_shielding(initial_intensity, material_thickness, attenuation_coeff):
        """Calculate radiation intensity after shielding"""
        return initial_intensity * np.exp(-attenuation_coeff * material_thickness)

    @staticmethod
    def decay_curve(initial_amount, half_life, time_points):
        """Calculate radioactive decay curve"""
        decay_constant = np.log(2) / half_life
        return initial_amount * np.exp(-decay_constant * time_points)

def main():
    calc = NuclearPhysicsCalculator()
    
    # Example 1: Water heating calculation
    print("Water Heating Analysis")
    print("=====================")
    
    test_energies = [1e6, 1e7, 1e8]  # Joules
    mass = 1.0  # kg
    
    for energy in test_energies:
        result = calc.calculate_water_temperature_rise(energy, mass)
        print(f"\nEnergy Input: {energy/1e6:.2f} MJ")
        print(f"Final Temperature: {result['final_temperature']:.2f}°C")
        print(f"Phase: {result['phase']}")
        if 'vapor_fraction' in result:
            print(f"Vapor Fraction: {result['vapor_fraction']:.2%}")
    
    # Example 2: Radiation Shielding
    print("\nRadiation Shielding Analysis")
    print("===========================")
    
    distances = np.linspace(0, 100, 100)
    intensities = [
        calc.calculate_radiation_shielding(1000, d, 0.02) for d in distances
    ]
    
    plt.figure(figsize=(10, 6))
    plt.plot(distances, intensities)
    plt.title('Radiation Intensity vs. Shielding Thickness')
    plt.xlabel('Shield Thickness (cm)')
    plt.ylabel('Radiation Intensity')
    plt.yscale('log')
    plt.grid(True)
    plt.show()
    
    # Example 3: Isotope Decay
    print("\nIsotope Decay Analysis")
    print("=====================")
    
    time_points = np.linspace(0, 10, 100)
    amount = calc.decay_curve(1000, 2, time_points)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, amount)
    plt.title('Radioactive Decay')
    plt.xlabel('Time (half-lives)')
    plt.ylabel('Amount Remaining')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
