# import codecademylib
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins=365)
plt.xlabel("Day of Year")
plt.ylabel("# of Flights")
plt.title("Flights Per Day")

plt.subplot(212)

plt.hist(in_bloom)
plt.xlabel("Day of Year")
plt.ylabel("Bloom Count")
plt.tight_layout()
plt.show()