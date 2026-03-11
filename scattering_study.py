"""
Scattering Study
Compute and plot scattering angle vs impact parameter
for multiple initial velocities.
"""

import numpy as np
import matplotlib.pyplot as plt

import simulation
import physics


# ============================================================
# Scattering Angle Computation
# ============================================================

def scattering_angle_from_final_p(p_M):
    """
    Compute scattering angle (radians) from final momentum.
    """
    v = physics.velocity_from_p(p_M)
    return np.arctan2(v[1], v[0])


# ============================================================
# Study Runner
# ============================================================

def run_study():

    # Velocities to test (percent of c)
    velocities = [10.0, 30.0, 60.0]

    # Impact parameter sweep
    impact_parameters = np.linspace(0.2, 3.0, 25)

    plt.figure(figsize=(8, 6))

    for v in velocities:

        angles = []

        print(f"Running velocity = {v}% of c")

        for b in impact_parameters:

            result = simulation.run(v, b)
            p_M_final = result["final_p_M"]

            theta = scattering_angle_from_final_p(p_M_final)
            angles.append(theta)

        # Convert to degrees
        angles_deg = np.degrees(angles)

        plt.plot(impact_parameters,
                 angles_deg,
                 label=f"{v}% c")

    plt.xlabel("Impact Parameter (b)")
    plt.ylabel("Scattering Angle (degrees)")
    plt.title("Scattering Angle vs Impact Parameter")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    run_study()