import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  levelsDF = pd.read_csv('epa-sea-level.csv')
  # print(levelsDF.head(10))
  # print(levelsDF.info())
  # print(levelsDF.describe())

  # Create scatter plot
  plt.scatter(levelsDF.Year, levelsDF['CSIRO Adjusted Sea Level'])
  # plt.show()

  # Create first line of best fit
  res = linregress(levelsDF.Year, levelsDF['CSIRO Adjusted Sea Level'])
  fitRange = pd.Series(i for i in range(1880, 2051))
  plt.plot(fitRange, res.intercept + res.slope*fitRange, label='fit 1')

  # Create second line of best fit
  res2 = linregress(levelsDF.Year[levelsDF.Year >= 2000], levelsDF['CSIRO Adjusted Sea Level'][levelsDF.Year >= 2000])
  fitRange2 = pd.Series(i for i in range(2000, 2051))
  plt.plot(fitRange2, res2.intercept + res2.slope*fitRange2, label='fit 2')

  # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.legend()
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()