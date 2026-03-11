"""
Physics module for the
Relativistic Two-Electron Planar Scattering Simulator

Relativistic momentum + central Coulomb force.
Momentum conserving.
Natural units: c = 1, m = 1, k = 1
"""

import numpy as np
import config


# ============================================================
# Relativistic Kinematics
# ============================================================

def gamma_from_p(p):
    p2 = np.dot(p, p)
    return np.sqrt(1.0 + p2)


def velocity_from_p(p):
    gamma = gamma_from_p(p)
    return p / gamma


# ============================================================
# Central Coulomb Force (Momentum Conserving)
# ============================================================

def compute_forces(r_R, p_R, r_M, p_M):
    """
    Compute equal-and-opposite Coulomb forces.
    """

    r_vec = r_R - r_M
    r2 = np.dot(r_vec, r_vec)
    r = np.sqrt(r2)

    if r < 1e-12:
        raise ValueError("Particles too close — singular force.")

    # Central force
    F_R = config.K_COULOMB * r_vec / (r**3)
    F_M = -F_R

    return F_R, F_M


# ============================================================
# Relativistic Acceleration
# ============================================================

def acceleration_from_force(p, F):
    """
    a = (F / gamma) - v (v·F) / gamma
    (natural units m=1, c=1)
    """

    gamma = gamma_from_p(p)
    v = velocity_from_p(p)

    term1 = F / gamma
    term2 = v * np.dot(v, F) / gamma

    return term1 - term2

# ============================================================
# Total Energy
# ============================================================

def total_energy(r_R, p_R, r_M, p_M):
    """
    Compute total relativistic energy:
    E = gamma_R + gamma_M + 1/r
    (natural units: m=1, k=1)
    """

    gamma_R = gamma_from_p(p_R)
    gamma_M = gamma_from_p(p_M)

    r_vec = r_R - r_M
    r = np.linalg.norm(r_vec)

    potential = config.K_COULOMB / r

    return gamma_R + gamma_M + potential