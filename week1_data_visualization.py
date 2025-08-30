import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated data for waste (tons), CO2 (ppm), energy demand (kWh)
dates = pd.date_range(start="2025-01-01", periods=30, freq="D")
data = pd.DataFrame({
    "date": dates,
    "waste": np.random.randint(50, 150, size=30),
    "co2": np.random.randint(300, 500, size=30),
    "energy_demand": np.random.randint(100, 300, size=30)
})

# Save data
data.to_csv("data/simulated_data.csv", index=False)

# Simple visualization
plt.plot(data["date"], data["waste"], label="Waste (tons)")
plt.plot(data["date"], data["energy_demand"], label="Energy Demand (kWh)")
plt.legend()
plt.show()
