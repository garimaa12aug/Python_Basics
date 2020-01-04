
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# Line plot
plt.plot([1,2,3,4],[3,4,5,6])
plt.xlabel('some numbers')
plt.ylabel('some numbers')
plt.show()


### Adding elements to line plots
t = np.arange(0.0, 2.0, 0.01) # Generate equally space numbers between 0 and 2
s = 1 + np.sin(2*np.pi*t)  # Apply sin function to the random numbers
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png") # Save a plot. Check the directory
plt.show()

#Bar Plot

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
x = range(len(y))
width = 1/1.5
plt.bar(x, y, width, color="blue")
plt.show()

#Scatter Plot

N = 50
# Generate random numbers
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

#Histogram
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000) # Generate random values with some distribution

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()

#Pie Chart

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


