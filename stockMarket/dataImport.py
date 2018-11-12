

import pandas
import matplotlib
import matplotlib.pyplot as plt
import seaborn

data = pandas.read_csv("/home/vegeta/NIFTYDATA/NSE_1-1-2010 to 28-12-2010.csv")

date = data["Date"]
c = data["Open"]
sharesTraded = data["Shares Traded"]
closingPrice = data["Close"]
openingPrice = data["Open"]
difference = closingPrice - openingPrice





fig, ax1 = plt.subplots()
#
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Difference', color=color)
ax1.plot(difference, color=color)
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





