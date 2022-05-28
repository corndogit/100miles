import matplotlib.pyplot as plt
import numpy as np


def main():
    # labels
    title_font = {'color': 'blue', 'size': 20}

    plt.title("100 Miles in May tracker", fontdict=title_font)
    plt.xlabel("Days into challenge")
    plt.ylabel("Cumulative mileage")

    # projected target
    projected_x = np.array([0, 30])
    projected_y = np.array([0, 100])

    # actual progress
    with open('miles.txt') as f:
        miles = [float(x) for x in f.readlines()]

    total_miles = []
    for x in range(len(miles)):
        if x != 0:
            total = miles[x] + sum(miles[0:x])
        else:
            total = miles[x]
        total_miles.append(total)

    def average_total(mileage):
        return sum(mileage) / len(mileage)

    actual_x = np.array(list(range(len(miles))))
    actual_y = np.array(total_miles)
    estimated_y = np.array([0, average_total(miles)*30])

    plt.plot(actual_x, actual_y, c='#54BB66', label=f"Current progress: {total_miles[-1]}/100 miles")
    plt.plot(projected_x, projected_y, c='#999999', label=f"Target: complete by day {round(100/average_total(miles))}")
    plt.plot(projected_x, estimated_y, c='#54BB66', ls='--', label=f"Projection of average ({round(average_total(miles), 2)} per day)")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
