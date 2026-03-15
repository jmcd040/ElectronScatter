"""
Relativistic electron interaction physics
version 3.0
"""

import numpy as np
import config


def gamma_from_p(p):
    p2 = np.dot(p, p)
    return np.sqrt(1 + p2 / config.MASS**2)


def velocity_from_p(p):
    gamma = gamma_from_p(p)
    return p / (gamma * config.MASS)


def acceleration_from_force(p, F):
    gamma = gamma_from_p(p)
    return F / (gamma * config.MASS)


def coulomb_force(r1, r2):

    dr = r1 - r2
    r = np.linalg.norm(dr)

    if r == 0:
        return np.zeros(2)

    return config.K_COULOMB * config.CHARGE**2 * dr / r**3


def compute_forces(r_R, p_R, r_M, p_M):

    F = coulomb_force(r_R, r_M)

    return F, -F