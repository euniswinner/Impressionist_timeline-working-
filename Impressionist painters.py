from matplotlib import pyplot as plt

Painter= ["Pissarro", "Manet", "Degas", "Cezanne", "Monet", "Renoir", "Cassatt"]
ST_Y = [1855, 1850, 1855, 1861, 1860, 1862, 1872]
durations = [48, 33, 57, 45, 66, 57, 54] 

plt.barh(Painter, durations, left=ST_Y)

plt.title("Active Years")
plt.show()