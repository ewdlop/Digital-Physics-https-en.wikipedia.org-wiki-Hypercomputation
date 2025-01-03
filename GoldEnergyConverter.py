class GoldEnergyConverter:
    def __init__(self):
        # Conversion constants
        self.METRIC_TON_TO_TROY_OUNCES = 32150.746
        self.ENERGY_PER_BARREL_GJ = 6.1  # Gigajoules per barrel of oil
        self.US_ANNUAL_ENERGY_PJ = 95000  # US annual energy consumption in Petajoules

    def metric_tons_to_troy_ounces(self, metric_tons):
        """Convert metric tons to troy ounces"""
        return metric_tons * self.METRIC_TON_TO_TROY_OUNCES

    def calculate_gold_value(self, troy_ounces, gold_price_per_ounce):
        """Calculate total value of gold in USD"""
        return troy_ounces * gold_price_per_ounce

    def calculate_oil_barrels(self, usd_value, oil_price_per_barrel):
        """Calculate equivalent barrels of oil"""
        return usd_value / oil_price_per_barrel

    def calculate_energy(self, oil_barrels):
        """Calculate energy in Gigajoules"""
        return oil_barrels * self.ENERGY_PER_BARREL_GJ

    def convert_to_petajoules(self, gigajoules):
        """Convert Gigajoules to Petajoules"""
        return gigajoules / 1e6

    def calculate_years_of_energy(self, petajoules):
        """Calculate equivalent years of US energy consumption"""
        return petajoules / self.US_ANNUAL_ENERGY_PJ

    def generate_report(self, gold_reserves, gold_price, oil_price):
        """Generate a complete analysis report"""
        # Perform calculations
        troy_ounces = self.metric_tons_to_troy_ounces(gold_reserves)
        gold_value = self.calculate_gold_value(troy_ounces, gold_price)
        oil_barrels = self.calculate_oil_barrels(gold_value, oil_price)
        energy_gj = self.calculate_energy(oil_barrels)
        energy_pj = self.convert_to_petajoules(energy_gj)
        years_of_energy = self.calculate_years_of_energy(energy_pj)

        # Format report
        report = f"""
Gold to Energy Conversion Report
==============================
Input Parameters:
----------------
Gold Reserves: {gold_reserves:,.2f} metric tons
Gold Price: ${gold_price:,.2f} per troy ounce
Oil Price: ${oil_price:,.2f} per barrel

Conversion Results:
-----------------
Gold in Troy Ounces: {troy_ounces:,.2f}
Total Gold Value: ${gold_value:,.2f}
Equivalent Oil Barrels: {oil_barrels:,.2f}
Energy Generation Potential: {energy_pj:,.2f} Petajoules
Years of US Energy Consumption: {years_of_energy:.2f}

Additional Metrics:
-----------------
Monthly Energy Coverage: {years_of_energy * 12:.1f} months
Daily Energy Equivalent: {energy_pj / 365:,.2f} Petajoules/day
"""
        return report

def main():
    # Current values (as of 2024)
    US_GOLD_RESERVES = 8133.5  # metric tons
    GOLD_PRICE = 2400  # USD per troy ounce
    OIL_PRICE = 80  # USD per barrel

    # Create converter instance
    converter = GoldEnergyConverter()
    
    # Generate and print report
    report = converter.generate_report(US_GOLD_RESERVES, GOLD_PRICE, OIL_PRICE)
    print(report)

    # Example of using with different values
    print("\nAlternative Scenario (with different prices):")
    alternative_report = converter.generate_report(
        US_GOLD_RESERVES,
        gold_price=2500,  # Higher gold price
        oil_price=70      # Lower oil price
    )
    print(alternative_report)

if __name__ == "__main__":
    main()
