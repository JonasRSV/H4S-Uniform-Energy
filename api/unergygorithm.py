import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import time
import pandas as pd
from IPython import display


def pdfs(day: np.ndarray, user_base: float) -> np.ndarray:
    daypdf = day / np.sum(np.abs(day))
    dpmax = np.max(daypdf)

    invdaypdf = (dpmax - daypdf) / np.sum(np.abs(dpmax - daypdf))

    int(user_base * len(day))
    daysize = len(day)

    print(user_base)

    std = np.exp(user_base)
    # if 0.5 > user_base >= 0.25:
        # std = 1.2
    # elif 0.75 > user_base >= 0.5:
        # std = 2
    # elif user_base >= 0.75:
        # std = 100 


    normalizer = lambda mean: (lambda x: \
            np.exp(-np.square(x - mean)/(2*std*std))/(std*np.sqrt(2*np.pi)))

    invdaypdf = np.array([
        np.sum(
            np.array(list(map(normalizer(i), np.arange(daysize)))) * invdaypdf)
        for i in range(len(day))
    ])

    invdaypdf = invdaypdf / np.sum(invdaypdf)
    return invdaypdf, daypdf


def demo(day: iter, fig, ax, axpdfs, speed=0.1, ipython=True):
    for usage in range(100):
        unergypdf, daypdf = pdfs(day, usage / 100.0)

        lamb = usage / 100

        avg = unergypdf * lamb + daypdf * (1 - lamb)

        axpdfs.cla()
        ax.cla()
        if ipython:
            display.clear_output(wait=True)

        ax.set_ylim([0, 0.3])
        ax.set_title("Percentage of users %d" % usage)

        sb.lineplot(np.arange(unergypdf.shape[0]), unergypdf, ax=axpdfs)
        sb.lineplot(np.arange(daypdf.shape[0]), daypdf, ax=axpdfs)

        sb.barplot(np.arange(avg.shape[0]), avg, ax=ax)
        plt.ylim([0, 0.3])

        if ipython:
            display.display(fig)
        else:
            plt.pause(0.001)

        time.sleep(speed)

    plt.show()


if __name__ == "__main__":
    fig, (ax, axpdfs) = plt.subplots(2)
    demo(np.sin(np.arange(24)) + 1, fig, ax, axpdfs, ipython=False)
