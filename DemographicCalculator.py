import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class PopulationParams:
    base_mortality_rate: float
    life_expectancy: float
    population_size: int
    age_distribution: Dict[str, float]
    healthcare_access: float  # 0 to 1
    infrastructure_quality: float  # 0 to 1

class DemographicCalculator:
    def __init__(self, params: PopulationParams):
        self.params = params
        self.age_groups = list(params.age_distribution.keys())
        
    def calculate_base_survival_rate(self, age_group: str) -> float:
        """Calculate base survival rate for an age group"""
        base_rate = 1.0 - self.params.base_mortality_rate
        
        # Adjust for age group
        age_factor = {
            '0-14': 0.99,
            '15-24': 0.98,
            '25-54': 0.97,
            '55-64': 0.95,
            '65+': 0.92
        }
        
        return base_rate * age_factor.get(age_group, 1.0)
    
    def adjust_for_resources(self, base_rate: float) -> float:
        """Adjust survival rate based on healthcare and infrastructure"""
        healthcare_factor = 0.95 + (0.05 * self.params.healthcare_access)
        infrastructure_factor = 0.95 + (0.05 * self.params.infrastructure_quality)
        
        return base_rate * healthcare_factor * infrastructure_factor
    
    def calculate_population_metrics(self) -> Dict:
        """Calculate various population metrics"""
        metrics = {}
        total_surviving = 0
        
        for age_group in self.age_groups:
            population_in_group = int(self.params.population_size * 
                                   self.params.age_distribution[age_group])
            
            base_rate = self.calculate_base_survival_rate(age_group)
            adjusted_rate = self.adjust_for_resources(base_rate)
            
            surviving = int(population_in_group * adjusted_rate)
            total_surviving += surviving
            
            metrics[age_group] = {
                'initial_population': population_in_group,
                'survival_rate': adjusted_rate,
                'surviving_population': surviving
            }
            
        metrics['total'] = {
            'initial_population': self.params.population_size,
            'survival_rate': total_surviving / self.params.population_size,
            'surviving_population': total_surviving
        }
        
        return metrics
    
    def plot_population_pyramid(self, metrics: Dict):
        """Create population pyramid before and after"""
        age_groups = [group for group in self.age_groups if group != 'total']
        initial_pop = [metrics[group]['initial_population'] for group in age_groups]
        final_pop = [metrics[group]['surviving_population'] for group in age_groups]
        
        y_pos = np.arange(len(age_groups))
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
        
        # Initial population
        ax1.barh(y_pos, initial_pop)
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(age_groups)
        ax1.set_title('Initial Population Distribution')
        
        # Final population
        ax2.barh(y_pos, final_pop)
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels(age_groups)
        ax2.set_title('Final Population Distribution')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self) -> str:
        """Generate a detailed report of the analysis"""
        metrics = self.calculate_population_metrics()
        
        report = "Population Demographics Analysis\n"
        report += "================================\n\n"
        
        report += "Input Parameters:\n"
        report += f"Base Mortality Rate: {self.params.base_mortality_rate:.2%}\n"
        report += f"Life Expectancy: {self.params.life_expectancy} years\n"
        report += f"Population Size: {self.params.population_size:,}\n"
        report += f"Healthcare Access Level: {self.params.healthcare_access:.2%}\n"
        report += f"Infrastructure Quality: {self.params.infrastructure_quality:.2%}\n\n"
        
        report += "Results by Age Group:\n"
        report += "--------------------\n"
        for age_group, data in metrics.items():
            if age_group != 'total':
                report += f"\n{age_group}:\n"
                report += f"  Initial Population: {data['initial_population']:,}\n"
                report += f"  Survival Rate: {data['survival_rate']:.2%}\n"
                report += f"  Final Population: {data['surviving_population']:,}\n"
        
        report += f"\nOverall Results:\n"
        report += f"Total Initial Population: {metrics['total']['initial_population']:,}\n"
        report += f"Average Survival Rate: {metrics['total']['survival_rate']:.2%}\n"
        report += f"Total Final Population: {metrics['total']['surviving_population']:,}\n"
        
        return report

def main():
    # Example parameters for a sample population
    params = PopulationParams(
        base_mortality_rate=0.01,
        life_expectancy=75.0,
        population_size=1000000,
        age_distribution={
            '0-14': 0.25,
            '15-24': 0.15,
            '25-54': 0.35,
            '55-64': 0.15,
            '65+': 0.10
        },
        healthcare_access=0.8,
        infrastructure_quality=0.75
    )
    
    # Create calculator instance
    calc = DemographicCalculator(params)
    
    # Generate and print report
    print(calc.generate_report())
    
    # Plot population distribution
    metrics = calc.calculate_population_metrics()
    calc.plot_population_pyramid(metrics)

if __name__ == "__main__":
    main()
