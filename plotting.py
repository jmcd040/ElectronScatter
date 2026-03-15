"""
Plotting utilities for Electron Scatter Simulation
Version: 3.0
"""
import matplotlib.pyplot as plt
import config

_initialized = False


def plot_trajectory(pos_R, pos_M, label):

    global _initialized

    if not _initialized:
        plt.figure(figsize=config.FIG_SIZE)
        _initialized = True

    plt.plot(pos_R[:,0], pos_R[:,1], label=f"R {label}")
    plt.plot(pos_M[:,0], pos_M[:,1], linestyle="--", label=f"M {label}")


def show():

    plt.gca().set_aspect("equal")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()