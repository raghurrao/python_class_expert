import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_distributions(df: pd.DataFrame, col: str, output_path: str):
    """
    Generate a Seaborn histplot of column 'col' in df, with KDE enabled.
    Save the figure to output_path.
    """
    plt.figure()
    sns.histplot(data=df, x=col, kde=True)
    plt.savefig(output_path)
    plt.close()