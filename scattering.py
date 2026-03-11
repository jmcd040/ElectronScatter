import numpy as np
import simulation
import integrator
import physics


def compute_scattering_angle(speed_percent, impact_parameter):
    """
    Run simulation and return scattering angle (radians).
    """

    data = simulation.run(speed_percent, impact_parameter)

    # Get final state by rerunning last state extraction logic
    # Easier: modify simulation.run() to also return final state