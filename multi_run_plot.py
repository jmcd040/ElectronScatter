"""
Plot multiple electron scattering runs on one figure.

Color encodes initial velocity of M.
Line style encodes impact parameter.

Both electrons share the same color for each run.
"""

import matplotlib.pyplot as plt
import simulation


# ============================================================
# Velocity → Color
# ============================================================

def velocity_to_color(speed_percent):

    vmax = 80.0
    v = min(max(speed_percent, 0.0), vmax) / vmax

    return plt.cm.plasma(v)


# ============================================================
# Impact parameter → Line style
# ============================================================

def impact_to_style(b):

    if b <= 1:
        return "-"
    elif b <= 2:
        return "--"
    else:
        return ":"


# ============================================================
# Main plotting routine
# ============================================================

def run_plot():

    velocities = [20, 40, 60, 80]
    impact_parameters = [1.0, 10.0]

    fig, ax = plt.subplots(figsize=(9.6, 7.2))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Electron Scattering Trajectories")

    ymin = 1e9
    ymax = -1e9
    xmin = 1e9
    xmax = -1e9

    for v in velocities:

        color = velocity_to_color(v)

        for b in impact_parameters:

            print(f"Running v={v}%  b={b}")

            result = simulation.run(v, b)

            pos_R = result["positions_R"]
            pos_M = result["positions_M"]

            style = impact_to_style(b)

            ax.plot(
                pos_R[:, 0], pos_R[:, 1],
                linestyle=style,
                color=color,
                linewidth=1.5,
                alpha=0.8
            )

            ax.plot(
                pos_M[:, 0], pos_M[:, 1],
                linestyle=style,
                color=color,
                linewidth=1.5,
                alpha=0.8
            )

            xmin = min(xmin, pos_R[:,0].min(), pos_M[:,0].min())
            xmax = max(xmax, pos_R[:,0].max(), pos_M[:,0].max())
            ymin = min(ymin, pos_R[:,1].min(), pos_M[:,1].min())
            ymax = max(ymax, pos_R[:,1].max(), pos_M[:,1].max())

    ax.set_xlim(xmin, xmax)

    # double vertical chart range (same style as renderer)
    y_center = 0.5 * (ymin + ymax)
    y_half = (ymax - ymin)

    ax.set_ylim(y_center - y_half, y_center + y_half)

    ax.grid(True)

    print("\nPlot complete. Close window when finished.")

    plt.show()


if __name__ == "__main__":
    print("multi_run_plot.py STARTED")
    run_plot()
