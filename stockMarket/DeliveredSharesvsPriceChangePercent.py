
import MarketDirectory.barPlot as barPlt
import  MarketDirectory.downloadFile as download
import pandas
import matplotlib.pyplot as plt
import numpy

filename = "/home/vegeta/NIFTYDATA/01-01-2015-TO-01-03-2015TATAMOTORSALLN.csv"
sharesDelivered = barPlt.fileParser(filename, "Deliverable Qty")

date = barPlt.fileParser(filename, "Date")
closingPrice = barPlt.fileParser(filename,"Close Price")
openingPrice = barPlt.fileParser(filename,"Open Price")
difference = closingPrice - openingPrice
differencePercentage = (difference / openingPrice) * 100

fig, ax1 = plt.subplots()
#
color = 'tab:red'
ax1.set_xlabel('time ')
ax1.set_ylabel('Closing Price', color=color)
ax1.plot(closingPrice, color=color)
ax1.tick_params(axis='y', labelcolor=color)

#
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
color = 'tab:blue'
ax2.set_ylabel('Closing Price', color=color)  # we already handled the x-label with ax1
ax2.plot(closingPrice, color=color)
ax2.tick_params(axis='y', labelcolor=color)

N = len(sharesDelivered)
x = range(N)
width = 0.3
plt.bar(x, sharesDelivered, width, color="blue")

plt.plot(closingPrice,color="yellow")


fig = plt.gcf()

plt.show()

sample = download.downloadCSV("https://www.quandl.com/api/v3/datasets/NSE/IBULISL.csv?api_key=KuTgzkSh6BkjfsSjYYxo")
data = pandas.read_csv(sample)
print(data)





