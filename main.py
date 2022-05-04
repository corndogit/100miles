import matplotlib.pyplot as plt
import numpy as np


def main():
    # labels
    title_font = {'color': 'blue', 'size': 20}

    plt.title("100 Miles in May tracker", fontdict=title_font)
    plt.xlabel("Days of the month")
    plt.ylabel("Cumulative mileage")

    # projected target
    projected_x = np.array([0, 30])
    projected_y = np.array([0, 100])

    # actual progress
    with open('miles.txt') as f:
        miles = [float(x) for x in f.readlines()]
        f.close()

    total_miles = []
    for x in range(len(miles)):
        if x != 0:
            total = miles[x] + sum(miles[0:x])
        else:
            total = miles[x]
        total_miles.append(total)

    actual_x = np.array(list(range(len(miles))))
    actual_y = np.array(total_miles)

    plt.plot(actual_x, actual_y, c='#54BB66')
    plt.plot(projected_x, projected_y, c='#999999')
    plt.show()


if __name__ == '__main__':
    main()
