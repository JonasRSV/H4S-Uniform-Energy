import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import time
import pandas as pd
from IPython import display


def unergyp(day: np.ndarray, user_base) -> float:

    daypdf = day / np.sum(np.abs(day))
    dpmax = np.max(daypdf)
    invdaypdf = (dpmax - daypdf) / np.sum(np.abs(dpmax - daypdf))

    window = int(user_base * len(day)) // 2
    invdaypdf = [
        np.mean(invdaypdf[max(i - window, 0):min(i + window, len(day))])
        for i in range(len(day))
    ]

    target = np.random.rand()

    point = np.argmin(np.abs(np.cumsum(invdaypdf) - target))

    return point


def pdfs(day: np.ndarray, user_base: float) -> np.ndarray:
    daypdf = day / np.sum(np.abs(day))
    dpmax = np.max(daypdf)

    invdaypdf = (dpmax - daypdf) / np.sum(np.abs(dpmax - daypdf))

    normalizer = np.exp( int(user_base * len(day)) // 2 
    invdaypdf = np.array([
        np.mean(invdaypdf[max(i - window, 0):min(i + window, len(day))])
        for i in range(len(day))
    ])
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

        sb.lineplot(np.arange(avg.shape[0]), avg, ax=ax)
        plt.ylim([0, 0.2])

        if ipython:
            display.display(fig)
        else:
            plt.pause(0.001)

        time.sleep(speed)

    plt.show()


if __name__ == "__main__":
    fig, (ax, axpdfs) = plt.subplots(2)
    demo(np.sin(np.arange(24)) + 1, fig, ax, axpdfs, ipython=False)
