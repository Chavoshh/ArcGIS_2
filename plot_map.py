import geopandas as gpd
import matplotlib.pyplot as plt

# Load a sample dataset from GeoPandas (world map)
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Filter (example: Europe only)
europe = world[world["continent"] == "Europe"]

# Plot
europe.plot(color="lightblue", edgecolor="black")
plt.title("Simple Map of Europe")
plt.show()
