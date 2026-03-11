"""
Simulation engine
version 3.0
"""

import numpy as np
import config
import integrator
import physics


def initialize(speed_percent, impact):

    speed_percent = speed_percent
    v = (speed_percent / 100) * config.C

    r_R = np.array([0.0, 0.0])
    p_R = np.zeros(2)

    r_M = np.array([-config.INITIAL_OFFSET_X, impact])

    gamma = 1 / np.sqrt(1 - v**2)

    p_M = np.array([gamma * config.MASS * v, 0.0])

    return integrator.pack_state(r_R, p_R, r_M, p_M)


def run(speed_percent, impact):

    state = initialize(speed_percent, impact)

    pos_R = []
    pos_M = []

    max_accel = 0
    step = 0

    while True:

        r_R, p_R, r_M, p_M = integrator.unpack_state(state)

        pos_R.append(r_R.copy())
        pos_M.append(r_M.copy())

        F_R, F_M = physics.compute_forces(r_R, p_R, r_M, p_M)

        a_R = physics.acceleration_from_force(p_R, F_R)
        a_M = physics.acceleration_from_force(p_M, F_M)

        accel = max(np.linalg.norm(a_R), np.linalg.norm(a_M))

        max_accel = max(max_accel, accel)

        if step > config.MIN_STEPS and accel < config.ACCELERATION_THRESHOLD * max_accel:
            break

        state = integrator.rk4_step(state, config.DT)
        step += 1

    return np.array(pos_R), np.array(pos_M)