"""
Configuration constants for the
Relativistic Two-Electron Planar Scattering Simulator
"""

# ============================================================
# Physical Constants (Natural Units)
# ============================================================

# Speed of light
C = 1.0

# Electron mass
MASS = 1.0

# Electron charge magnitude
CHARGE = 1.0   # sign handled in physics module

# Coulomb constant (1 / (4*pi*epsilon_0))
K_COULOMB = 1.0

# Magnetic constant factor (mu_0 / (4*pi))
MU_FACTOR = 1.0  # consistent with natural unit scaling


# ============================================================
# Numerical Parameters
# ============================================================

# Fixed timestep for RK4 integration
DT = 1.0e-2

# Acceleration threshold fraction for termination (1%)
ACCELERATION_THRESHOLD = 0.01

# Minimum number of steps before allowing termination
MIN_STEPS = 100


# ============================================================
# Initial Condition Defaults
# ============================================================

# Initial x-position offset for projectile electron M
X0 = 50.0

# Default impact parameter
DEFAULT_IMPACT_PARAMETER = 10.0

# Default initial speed of M (fraction of c)
DEFAULT_SPEED_PERCENT = 30.0  # 30% of c

# Maximum allowed speed percent
MAX_SPEED_PERCENT = 80.0


# ============================================================
# Rendering Parameters
# ============================================================

# Axis margin fraction (5%)
AXIS_MARGIN_FRACTION = 0.05

# Playback speed bounds
PLAYBACK_MIN = 1
PLAYBACK_MAX = 10
