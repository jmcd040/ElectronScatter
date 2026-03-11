"""
python3 test_harness.py
Verification test harness for
Relativistic Two-Electron Scattering Simulator
"""

import numpy as np
import simulation
import integrator
import physics
import config

print("DT =", config.DT)

# ============================================================
# Momentum Conservation Test
# ============================================================

def test_momentum_conservation(speed_percent=10.0,
                               impact_parameter=1.0):

    print("Running momentum conservation test...")
    print(f"Speed = {speed_percent}% of c")
    print(f"Impact parameter = {impact_parameter}")
    print()

    state = simulation.initialize_state(speed_percent,
                                        impact_parameter)

    dt = config.DT

    total_p_initial = None
    total_p_final = None

    max_accel = 0.0
    step_count = 0

    while True:

        r_R, p_R, r_M, p_M = integrator.unpack_state(state)

        total_p = p_R + p_M

        if total_p_initial is None:
            total_p_initial = total_p.copy()

        # Compute forces and acceleration
        F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)
        a_R = physics.acceleration_from_force(p_R, F_R)
        a_M = physics.acceleration_from_force(p_M, F_M)

        accel_mag = max(np.linalg.norm(a_R),
                        np.linalg.norm(a_M))

        if accel_mag > max_accel:
            max_accel = accel_mag

        if (step_count > config.MIN_STEPS and
            accel_mag <= config.ACCELERATION_THRESHOLD * max_accel):
            total_p_final = total_p.copy()
            break

        state = integrator.rk4_step(state, dt)
        step_count += 1

    print("Initial total momentum:", total_p_initial)
    print("Final total momentum:  ", total_p_final)

    delta_p = total_p_final - total_p_initial
    print("Momentum difference:   ", delta_p)
    print("Relative error:        ",
          np.linalg.norm(delta_p) /
          (np.linalg.norm(total_p_initial) + 1e-12))

    print()
    print("Test complete.")
    print("-" * 40)


# ============================================================
# Force Symmetry Test
# ============================================================

def test_force_symmetry():

    print("Running force symmetry test...")
    print()

    state = simulation.initialize_state(10.0, 1.0)

    r_R, p_R, r_M, p_M = integrator.unpack_state(state)

    F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)

    print("F_R:", F_R)
    print("F_M:", F_M)
    print("F_R + F_M:", F_R + F_M)

    print()
    print("Magnitude of violation:",
          np.linalg.norm(F_R + F_M))
    print("-" * 40)

# ============================================================
# Energy Conservation Test
# ============================================================

def test_energy_conservation(speed_percent=10.0,
                             impact_parameter=1.0):

    print("Running energy conservation test...")
    print(f"Speed = {speed_percent}% of c")
    print(f"Impact parameter = {impact_parameter}")
    print()

    state = simulation.initialize_state(speed_percent,
                                        impact_parameter)

    dt = config.DT

    r_R, p_R, r_M, p_M = integrator.unpack_state(state)
    E_initial = physics.total_energy(r_R, p_R, r_M, p_M)

    max_accel = 0.0
    step_count = 0

    while True:

        r_R, p_R, r_M, p_M = integrator.unpack_state(state)

        F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)
        a_R = physics.acceleration_from_force(p_R, F_R)
        a_M = physics.acceleration_from_force(p_M, F_M)

        accel_mag = max(np.linalg.norm(a_R),
                        np.linalg.norm(a_M))

        if accel_mag > max_accel:
            max_accel = accel_mag

        if (step_count > config.MIN_STEPS and
            accel_mag <= config.ACCELERATION_THRESHOLD * max_accel):
            break

        state = integrator.rk4_step(state, dt)
        step_count += 1

    r_R, p_R, r_M, p_M = integrator.unpack_state(state)
    E_final = physics.total_energy(r_R, p_R, r_M, p_M)

    delta_E = E_final - E_initial
    rel_error = abs(delta_E) / abs(E_initial)

    print("Initial Energy:", E_initial)
    print("Final Energy:  ", E_final)
    print("Energy diff:   ", delta_E)
    print("Relative error:", rel_error)
    print("-" * 40)
# ============================================================
# Run Tests
# ============================================================

if __name__ == "__main__":
    test_force_symmetry()
    test_momentum_conservation(speed_percent=10.0, impact_parameter=1.0)
    test_momentum_conservation(speed_percent=30.0, impact_parameter=1.0)
    test_energy_conservation(10.0, 1.0)
    test_energy_conservation(30.0, 1.0)