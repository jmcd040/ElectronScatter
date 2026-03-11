"""
RK4 integrator for two-particle system
version 3.0
"""

import numpy as np
import physics


def pack_state(r1, p1, r2, p2):

    return np.concatenate([r1, p1, r2, p2])


def unpack_state(state):

    r1 = state[0:2]
    p1 = state[2:4]
    r2 = state[4:6]
    p2 = state[6:8]

    return r1, p1, r2, p2


def derivatives(state):

    r1, p1, r2, p2 = unpack_state(state)

    v1 = physics.velocity_from_p(p1)
    v2 = physics.velocity_from_p(p2)

    F1, F2 = physics.compute_forces(r1, p1, r2, p2)

    return pack_state(v1, F1, v2, F2)


def rk4_step(state, dt):

    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)

    return state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)