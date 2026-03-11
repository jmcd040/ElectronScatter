"""
Main entry point for Electron Scatter Simulation
Version: 3.0
"""
import config
import simulation
import plotting


def main():

    for v in config.VELOCITIES:
        for impact in config.IMPACT_PARAMETERS:

            pos_R, pos_M = simulation.run(v, impact)

            label = f"v={v}%  b={impact}"

            plotting.plot_trajectory(pos_R, pos_M, label)

    plotting.show()


if __name__ == "__main__":
    main()