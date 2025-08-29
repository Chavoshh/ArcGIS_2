import geopandas as gpd
import matplotlib.pyplot as plt

# Load shapefile from the data folder
world = gpd.read_file("data/ne_110m_admin_0_boundary_lines_land.shp")

# Plot
world.plot(color="lightblue", edgecolor="black")
plt.title("World Boundary Lines (Natural Earth)")
plt.show()
