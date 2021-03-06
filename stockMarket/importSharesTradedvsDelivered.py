

import pandas
import matplotlib.pyplot as plt
import numpy

data = pandas.read_csv("/home/vegeta/NIFTYDATA/01-01-2015-TO-01-03-2015TATAMOTORSALLN.csv")


date = data["Date"]

deliveredRatio = data["% Dly Qt to Traded Qty"]
sharesTraded = data["Total Traded Quantity"]
closingPrice = data["Close Price"]
openingPrice = data["Open Price"]
difference = closingPrice - openingPrice

print(data.shape)

fig, ax1 = plt.subplots()
#
color = 'tab:red'
ax1.set_xlabel('time ')
ax1.set_ylabel('Delivered Ratio', color=color)
ax1.plot(deliveredRatio, color=color)
ax1.tick_params(axis='y', labelcolor=color)
#
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
color = 'tab:blue'
ax2.set_ylabel('Shares Traded', color=color)  # we already handled the x-label with ax1
ax2.plot(sharesTraded, color=color)
ax2.tick_params(axis='y', labelcolor=color)


plt.show()

#print(data.corr())
print(difference.corr(sharesTraded))
#fig.tight_layout()  # otherwise the right y-label is slightly clipped





