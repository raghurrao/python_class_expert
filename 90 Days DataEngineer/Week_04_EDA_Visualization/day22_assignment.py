import matplotlib.pyplot as plt
import numpy as np

def plot_pricing_trends(filename: str):
    # Plot mock line graph and save to filename
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.savefig(filename)
    plt.close()
