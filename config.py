"""
Configuration for Electron Scatter Simulation
Version: 3.0
"""
# ==============================
# Environment setup control
# ==============================
# If False, env_setup.py will skip creating the venv
# and installing dependencies.
ENABLE_ENV_SETUP = False

# ==============================
# Upper limit for initial velocity of electron M as a percentage of C
# ==============================
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
MIN_STEPS = 250
ACCELERATION_THRESHOLD = 0.01

# ==============================
# Initial geometry
# ==============================
# Initial separation of electron M from R along x-axis
INITIAL_OFFSET_X = 50.0

# ==============================
# Simulation parameters
# for multiple runs, enter a list 
# of comma separated values
# ==============================
VELOCITIES = [
    30
]

IMPACT_PARAMETERS = [
    5,25
]

# ==============================
# Plot settings
# ==============================
FIG_SIZE = (6,6)
AXIS_MARGIN = 0.05
