import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,edgecolor='none',s=10)

plt.title("square numbers",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("Squares of value",fontsize = 14)

plt.tick_params(axis='both',which = 'major', labelsize=14)
plt.axis([0,1100,0,1100000])

plt.show()
