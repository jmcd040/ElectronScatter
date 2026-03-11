"""
Entry point for the
Relativistic Two-Electron Planar Scattering Simulator
"""

import config
import simulation
import renderer


# ============================================================
# User Input Helpers
# ============================================================

def get_float(prompt, default):
    """
    Get float input with default fallback.
    """
    try:
        value = input(f"{prompt} [default={default}]: ")
        if value.strip() == "":
            return default
        return float(value)
    except ValueError:
        print("Invalid input. Using default.")
        return default


# ============================================================
# Main
# ============================================================

def main():
    import renderer

    print("MAIN.PY STARTED")
    print("Renderer module loaded from:", renderer.__file__)
    print("\nRelativistic Two-Electron Scattering Simulator\n")

    speed_percent = get_float(
        f"Initial speed of M (0–{config.MAX_SPEED_PERCENT}% of c)",
        config.DEFAULT_SPEED_PERCENT
    )

    impact_parameter = get_float(
        "Impact parameter (b)",
        config.DEFAULT_IMPACT_PARAMETER
    )

    playback_speed = get_float(
        f"Playback speed ({config.PLAYBACK_MIN}–{config.PLAYBACK_MAX})",
        5
    )

    print("\nRunning simulation...\n")

    sim_data = simulation.run(speed_percent, impact_parameter)

    print("Simulation complete. Launching animation...\n")

    renderer.animate(sim_data, playback_speed, speed_percent)

if __name__ == "__main__":
    main()