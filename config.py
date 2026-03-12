"""
Configuration for Electron Scatter Simulation
Version: 3.0
"""

MAX_SPEED_PERCENT = 80
# ==============================
# Physical constants
# ==============================
C = 1.0
MASS = 1.0
CHARGE = 1.0
K_COULOMB = 1.0

# ==============================
# Numerical integration
# ==============================
DT = 0.01
MIN_STEPS = 100
ACCELERATION_THRESHOLD = 0.01

# ==============================
# Initial geometry
# ==============================
INITIAL_OFFSET_X = 10.0

# ==============================
# Simulation parameters
# for multiple runs, enter a list 
# of comma separated values
# ==============================
VELOCITIES = [
    30,60
]

IMPACT_PARAMETERS = [
    5
]

# ==============================
# Plot settings
# ==============================
FIG_SIZE = (6,6)
AXIS_MARGIN = 0.05
