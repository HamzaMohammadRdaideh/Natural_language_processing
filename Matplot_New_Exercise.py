
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import sqrt

# # Draw a line in a diagram from position (0,0) to position (6,250):
# xpoints = np.array([0 ,6])
# ypoints = np.array([0 ,250])

# plt.plot(xpoints, ypoints)
# plt.show()

# # Without line
# plt.plot(xpoints, ypoints ,'o')
# plt.show()

# # Multiple point
# x = np.array([1,2,3,4,5])
# y = np.array([6,7,8,3,10])

# plt.plot(x ,y)
# plt.show()


# # Default X-Points
# # If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3,

# r = np.array([4,1,9,11])
# plt.plot(r)
# plt.show()


# # Matplotlib Markers

# x = np.array([1,2,3,4,5])
# y = np.array([6,7,8,3,10])

# plt.plot(x ,y ,marker = '*')
# plt.show()

# # Format Strings fmt  marker|line|color 

# plt.plot(x ,y ,'o:r')
# plt.show()

# # Marker Size and color markeredgecolor

# plt.plot(x ,y ,'o:r' ,ms = 20 ,mec = 'b')
# plt.show()


# # Linestyle linestyle, or shorter ls ,dashed ,dotted ,solid (default)
# # Line Color color or c 

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dotted' ,c = 'r')
# plt.show()

# # Multiple Lines

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)
# plt.show()


# # Matplotlib Labels and Title and set font => fontdict
# # Position the Title => loc

# a = np.array([10,20,30,40,50,60,70,80,90])
# b = np.array([1,2,3,4,5,6,7,8,9])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.plot(a ,b ,'o:g')
# plt.xlabel('Cost' ,fontdict = font1)
# plt.ylabel('Spped' ,fontdict = font1)
# plt.title('RDH' ,fontdict = font2 ,loc ='left')

# # Matplotlib Adding Grid Lines
# plt.grid()
# plt.show()


# # Specify Which Grid Lines to Display
# # You can use the axis parameter in the grid() function to specify which grid lines to display.

# a1 = np.array([10,20,30,40,50])
# b1 = np.array([1,2,3,4,5])

# plt.plot(a1 ,b1)
# plt.grid(axis = x)
# plt.show()


# Display Multiple Plots
# With the subplots() function you can draw multiple plots in one figure:
# plt.subplot(1, 2, 1)
# the figure has 1 row, 2 columns, and this plot is the first plot. 

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()


# # Matplotlib Scatter
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()


# # Compare Plots
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y ,color = 'hotpink')

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y ,color = 'green')

# plt.show() 


# # Matplotlib Bars

# a = np.array([1,2,3,4,5])
# b = np.array([7,2,5,9,1])

# plt.bar(a ,b)
# plt.show()

# # Horizontal Bars barh() and color
# a = np.array(['A' ,'B' ,'C' ,'D'])
# b = np.array([7,2,5,9,])

# plt.barh(a ,b ,color = 'black')
# plt.show()


# Matplotlib Histograms
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()


# Matplotlib Pie Charts

y = np.array([35, 25, 25, 15])
my_label = ['A' ,'B' ,'C' ,'D']

plt.pie(y ,labels = my_label)
plt.show() 

# Explode
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.legend(loc = 'upper left' ,title = 'Fruits')
plt.show() 

