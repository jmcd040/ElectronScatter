"""
Simulation controller for the
Relativistic Two-Electron Planar Scattering Simulator
"""

import numpy as np
import config
import physics
import integrator


# ============================================================
# Initialization
# ============================================================

def initialize_state(speed_percent, impact_parameter):
    """
    Create initial system state.
    """

    # Clamp speed
    speed_percent = min(speed_percent, config.MAX_SPEED_PERCENT)

    v = (speed_percent / 100.0) * config.C

    # Electron R (at rest at origin)
    r_R = np.array([0.0, 0.0])
    p_R = np.array([0.0, 0.0])

    # Electron M (incoming from left)
    r_M = np.array([-config.X0, impact_parameter])
    gamma = 1.0 / np.sqrt(1.0 - v**2)
    p_M = np.array([gamma * config.MASS * v, 0.0])

    return integrator.pack_state(r_R, p_R, r_M, p_M)


# ============================================================
# Simulation Loop
# ============================================================

def run(speed_percent, impact_parameter):
    """
    Run full simulation until termination condition met.
    Returns trajectory data and axis limits.
    """

    state = initialize_state(speed_percent, impact_parameter)

    dt = config.DT

    positions_R = []
    positions_M = []

    max_accel = 0.0
    step_count = 0

    while True:

        r_R, p_R, r_M, p_M = integrator.unpack_state(state)

        # Store positions
        positions_R.append(r_R.copy())
        positions_M.append(r_M.copy())

        # Compute forces
        F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)

        # Compute accelerations
        a_R = physics.acceleration_from_force(p_R, F_R)
        a_M = physics.acceleration_from_force(p_M, F_M)

        accel_mag = max(np.linalg.norm(a_R),
                        np.linalg.norm(a_M))

        # Track maximum acceleration
        if accel_mag > max_accel:
            max_accel = accel_mag

        # Termination condition
        if (step_count > config.MIN_STEPS and
            accel_mag <= config.ACCELERATION_THRESHOLD * max_accel):
            break

        # Advance state
        state = integrator.rk4_step(state, dt)

        step_count += 1

    positions_R = np.array(positions_R)
    positions_M = np.array(positions_M)

    axis_limits = compute_axis_limits(positions_R, positions_M)
    
    r_R, p_R, r_M, p_M = integrator.unpack_state(state)

    return {
        "positions_R": positions_R,
        "positions_M": positions_M,
        "axis_limits": axis_limits,
        "final_p_R":   p_R,
        "final_p_M":   p_M
    }


# ============================================================
# Axis Scaling
# ============================================================

def compute_axis_limits(pos_R, pos_M):
    """
    Compute fixed axis limits with 5% margin.
    """

    all_x = np.concatenate([pos_R[:, 0], pos_M[:, 0]])
    all_y = np.concatenate([pos_R[:, 1], pos_M[:, 1]])

    min_x, max_x = np.min(all_x), np.max(all_x)
    min_y, max_y = np.min(all_y), np.max(all_y)

    dx = max_x - min_x
    dy = max_y - min_y

    margin_x = config.AXIS_MARGIN_FRACTION * dx
    margin_y = config.AXIS_MARGIN_FRACTION * dy

    return (
        min_x - margin_x,
        max_x + margin_x,
        min_y - margin_y,
        max_y + margin_y
    )