import numpy as np
import matplotlib.pyplot as plt

class IsotopeDecayCalculator:
    def __init__(self):
        # Common medical isotopes with half-lives in hours
        self.medical_isotopes = {
            "Tc-99m": 6.0,      # Used in medical imaging
            "I-131": 192.0,     # Used in thyroid treatment
            "F-18": 1.83,       # Used in PET scans
            "Y-90": 64.0,       # Used in cancer treatment
            "Mo-99": 66.0       # Used as Tc-99m generator
        }

    def calculate_decay(self, initial_amount, half_life_hours, time_hours):
        """Calculate remaining amount after decay"""
        decay_constant = np.log(2) / half_life_hours
        return initial_amount * np.exp(-decay_constant * time_hours)

    def plot_decay_curve(self, isotope_name, initial_amount, duration_hours):
        """Plot decay curve for a specific isotope"""
        if isotope_name not in self.medical_isotopes:
            raise ValueError(f"Unknown isotope: {isotope_name}")

        half_life = self.medical_isotopes[isotope_name]
        times = np.linspace(0, duration_hours, 1000)
        amounts = self.calculate_decay(initial_amount, half_life, times)

        plt.figure(figsize=(10, 6))
        plt.plot(times, amounts)
        plt.title(f'Decay Curve for {isotope_name} (Half-life: {half_life} hours)')
        plt.xlabel('Time (hours)')
        plt.ylabel('Remaining Amount (arbitrary units)')
        plt.grid(True)
        
        # Add half-life markers
        plt.axhline(y=initial_amount/2, color='r', linestyle='--', alpha=0.3)
        plt.axvline(x=half_life, color='r', linestyle='--', alpha=0.3)
        
        # Add annotation for half-life
        plt.annotate(f'Half-life: {half_life} hours', 
                    xy=(half_life, initial_amount/2),
                    xytext=(half_life+duration_hours/10, initial_amount/2),
                    arrowprops=dict(facecolor='red', shrink=0.05))
        
        plt.show()

    def compare_isotopes(self, initial_amount=1000, duration_hours=24):
        """Compare decay rates of different medical isotopes"""
        plt.figure(figsize=(12, 8))
        
        for isotope, half_life in self.medical_isotopes.items():
            times = np.linspace(0, duration_hours, 1000)
            amounts = self.calculate_decay(initial_amount, half_life, times)
            plt.plot(times, amounts, label=f'{isotope} (t½={half_life}h)')

        plt.title('Comparison of Medical Isotope Decay Rates')
        plt.xlabel('Time (hours)')
        plt.ylabel('Remaining Amount (arbitrary units)')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')
        plt.show()

    def calculate_activity_time(self, isotope_name, initial_amount, target_fraction):
        """Calculate time needed to reach a target fraction of initial amount"""
        half_life = self.medical_isotopes[isotope_name]
        decay_constant = np.log(2) / half_life
        time = -np.log(target_fraction) / decay_constant
        return time

def main():
    calc = IsotopeDecayCalculator()
    
    # Example 1: Plot decay curve for Tc-99m
    print("Analyzing Tc-99m decay (common medical imaging isotope)")
    calc.plot_decay_curve("Tc-99m", 1000, 24)
    
    # Example 2: Compare different medical isotopes
    print("\nComparing decay rates of different medical isotopes")
    calc.compare_isotopes()
    
    # Example 3: Calculate specific decay times
    print("\nTime to reach specific activity levels for Tc-99m:")
    initial = 1000
    for fraction in [0.5, 0.25, 0.1, 0.01]:
        time = calc.calculate_activity_time("Tc-99m", initial, fraction)
        print(f"Time to reach {fraction*100}% activity: {time:.2f} hours")

if __name__ == "__main__":
    main()
