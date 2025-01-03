import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Material:
    """Class to store material properties for radiation shielding"""
    name: str
    density: float  # g/cm³
    attenuation_coefficient: float  # cm²/g
    cost_per_cm3: float  # dollars per cm³

class RadiationShield:
    def __init__(self):
        # Common shielding materials with their properties
        self.materials = {
            "concrete": Material("Concrete", 2.3, 0.0573, 0.02),
            "lead": Material("Lead", 11.34, 0.0959, 0.25),
            "water": Material("Water", 1.0, 0.0706, 0.001),
            "steel": Material("Steel", 7.874, 0.0706, 0.15),
            "earth": Material("Earth", 1.6, 0.0512, 0.001)
        }
    
    def calculate_attenuation(self, initial_intensity, material_name, thickness):
        """
        Calculate radiation intensity after passing through shielding
        Using the Beer-Lambert law: I = I₀ * e^(-μρx)
        
        Parameters:
        initial_intensity: Initial radiation intensity
        material_name: Name of shielding material
        thickness: Shield thickness in cm
        
        Returns:
        final_intensity: Radiation intensity after shielding
        """
        material = self.materials[material_name]
        mu = material.attenuation_coefficient
        rho = material.density
        
        final_intensity = initial_intensity * np.exp(-mu * rho * thickness)
        return final_intensity
    
    def calculate_required_thickness(self, initial_intensity, target_intensity, material_name):
        """Calculate required thickness to achieve desired radiation reduction"""
        material = self.materials[material_name]
        mu = material.attenuation_coefficient
        rho = material.density
        
        # Rearranged Beer-Lambert law to solve for thickness
        thickness = -np.log(target_intensity / initial_intensity) / (mu * rho)
        return thickness
    
    def compare_materials(self, initial_intensity, target_intensity):
        """Compare different materials for achieving target radiation reduction"""
        results = []
        
        for material_name in self.materials:
            thickness = self.calculate_required_thickness(
                initial_intensity, target_intensity, material_name
            )
            material = self.materials[material_name]
            volume = thickness * 100 * 100  # Assuming 1m x 1m shield
            cost = volume * material.cost_per_cm3
            
            results.append({
                'material': material_name,
                'thickness_cm': thickness,
                'cost_usd': cost,
                'weight_kg': volume * material.density / 1000
            })
        
        return results

    def plot_attenuation_curves(self, initial_intensity, max_thickness=100):
        """Plot attenuation curves for different materials"""
        thicknesses = np.linspace(0, max_thickness, 1000)
        plt.figure(figsize=(10, 6))
        
        for material_name in self.materials:
            intensities = [
                self.calculate_attenuation(initial_intensity, material_name, t)
                for t in thicknesses
            ]
            plt.plot(thicknesses, intensities, label=material_name.capitalize())
        
        plt.xlabel('Shield Thickness (cm)')
        plt.ylabel('Radiation Intensity (relative units)')
        plt.title('Radiation Attenuation by Material')
        plt.yscale('log')
        plt.grid(True)
        plt.legend()
        plt.show()

def main():
    shield = RadiationShield()
    
    # Example calculations
    initial_intensity = 1000  # arbitrary units
    target_intensity = 1  # target reduction to 0.1% of initial
    
    print("Radiation Shielding Analysis")
    print("===========================")
    print(f"Initial Intensity: {initial_intensity}")
    print(f"Target Intensity: {target_intensity}")
    print("\nRequired shielding for different materials:")
    
    results = shield.compare_materials(initial_intensity, target_intensity)
    
    # Display results in a formatted table
    print("\n{:<10} {:<15} {:<15} {:<15}".format(
        "Material", "Thickness (cm)", "Weight (kg)", "Cost (USD)"
    ))
    print("-" * 55)
    
    for result in results:
        print("{:<10} {:<15.2f} {:<15.2f} {:<15.2f}".format(
            result['material'].capitalize(),
            result['thickness_cm'],
            result['weight_kg'],
            result['cost_usd']
        ))
    
    # Plot attenuation curves
    shield.plot_attenuation_curves(initial_intensity)

if __name__ == "__main__":
    main()
