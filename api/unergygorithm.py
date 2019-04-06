import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import time
import pandas as pd
import sys
from IPython import display


def pdfs(day: np.ndarray, user_base: float) -> np.ndarray:
    daypdf = day / np.sum(np.abs(day))
    dpmax = np.max(daypdf)

    invdaypdf = (dpmax - daypdf) / np.sum(np.abs(dpmax - daypdf))




    # invdaypdf = invdaypdf / np.sum(invdaypdf)
    return invdaypdf, daypdf


def demo(day: iter, fig, axpdfs, speed=0.1, ipython=True):
    for usage in range(50):
        unergypdf, daypdf = pdfs(day, usage / 100.0)

        lamb = usage / 100

        avg = unergypdf * lamb + daypdf * (1 - lamb)

        axpdfs.cla()
        # ax.cla()
        if ipython:
            display.clear_output(wait=True)

        ax.set_ylim([0, 0.3])
        # ax.set_title("Percentage of users %d" % (usage * 2))

        sb.lineplot(np.arange(unergypdf.shape[0]), unergypdf, markers="-", dashes=True, ax=axpdfs)
        sb.lineplot(np.arange(daypdf.shape[0]), daypdf, markers="-", dashes=True, ax=axpdfs)

        # sb.barplot(np.arange(avg.shape[0]), avg, ax=ax)
        plt.ylim([0, 0.3])

        if ipython:
            display.display(fig)
        else:
            plt.pause(0.001)


        time.sleep(speed)
        # sys.exit(0)

    plt.show()


if __name__ == "__main__":
    #fig, (ax, axpdfs) = plt.subplots(2)
    # sb.set_style("whitegrid")
    sb.set()
    fig, ax = plt.subplots(1)
    demo(np.sin(np.arange(24)) + 1, fig, ax, ipython=False)
