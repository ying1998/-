import matplotlib.pyplot as plt
input_values = list(range(1,5001))
cubes = [x**3 for x in input_values ]

plt.scatter(input_values,cubes,c=cubes,cmap = plt.cm.Blues,edgecolor='none',s=10)
plt.title("cube numbers",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("Cubes of value",fontsize = 14)

plt.tick_params(axis='both',which = 'major', labelsize=14)
plt.axis([0,5200,0,5200**3])
plt.show()
