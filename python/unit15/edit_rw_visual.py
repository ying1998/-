import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    # print("this is point_numbers: %s " % point_numbers)
    # print("this is rw.y_values :%s "%rw.y_values)
    plt.plot(rw.x_values, rw.y_values,linewidth =1)
    

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk ?(y/n):")
    if keep_running == 'n':
        break
