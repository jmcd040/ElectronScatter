"""
RK4 Integrator for the
Relativistic Two-Electron Planar Scattering Simulator
"""

import numpy as np
import physics


# ============================================================
# State Utilities
# ============================================================

def pack_state(r_R, p_R, r_M, p_M):
    """
    Pack system state into a flat vector.
    Order:
    [r_R(2), p_R(2), r_M(2), p_M(2)]
    """
    return np.concatenate([r_R, p_R, r_M, p_M])


def unpack_state(state):
    """
    Unpack flat state vector into components.
    """
    r_R = state[0:2]
    p_R = state[2:4]
    r_M = state[4:6]
    p_M = state[6:8]
    return r_R, p_R, r_M, p_M


# ============================================================
# Time Derivative
# ============================================================

def derivatives(state):
    """
    Compute time derivatives of the full state.
    Returns d(state)/dt as flat vector.
    """

    r_R, p_R, r_M, p_M = unpack_state(state)

    # Velocities
    v_R = physics.velocity_from_p(p_R)
    v_M = physics.velocity_from_p(p_M)

    # Forces
    F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)

    # Time derivatives
    dr_R_dt = v_R
    dp_R_dt = F_R
    dr_M_dt = v_M
    dp_M_dt = F_M

    return pack_state(dr_R_dt, dp_R_dt, dr_M_dt, dp_M_dt)


# ============================================================
# RK4 Step
# ============================================================

def rk4_step(state, dt):
    """
    Advance system state by one timestep using RK4.
    """

    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)

    new_state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return new_state