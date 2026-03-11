"""
Renderer for the
Relativistic Two-Electron Planar Scattering Simulator
version 1.0
"""

import matplotlib
matplotlib.use("TkAgg")  # force GUI backend

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import config


# ============================================================
# Velocity → Color Mapping
# ============================================================

def velocity_to_color(speed_percent):
    """
    Map velocity (0–80% c) to a color.
    Uses the plasma colormap.
    """

    vmax = 80.0
    v = min(max(speed_percent, 0.0), vmax) / vmax

    return plt.cm.plasma(v)


# ============================================================
# Playback Mapping
# ============================================================

def playback_to_interval(playback_speed):
    """
    Map playback speed (1–10) to frame interval (ms).
    1 = slow, 10 = fast.
    """

    playback_speed = max(1, min(10, playback_speed))

    return 100 - (playback_speed - 1) * 8


# ============================================================
# Animation
# ============================================================

def animate(simulation_data, playback_speed=5, speed_percent=30.0):
    print("animate() function started")
    pos_R = simulation_data["positions_R"]
    pos_M = simulation_data["positions_M"]
    xmin, xmax, ymin, ymax = simulation_data["axis_limits"]

    # Determine color from velocity
    color = velocity_to_color(speed_percent)

    # Create figure (20% larger than default)
    fig, ax = plt.subplots(figsize=(9.6, 7.2))

    ax.set_xlim(xmin, xmax)

    # Double vertical chart range
    y_center = 0.5 * (ymin + ymax)
    y_half = (ymax - ymin)
    ax.set_ylim(y_center - y_half, y_center + y_half)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Relativistic Two-Electron Scattering")

    # Points and trails
    point_R, = ax.plot([], [], marker='o', linestyle='', color=color)
    point_M, = ax.plot([], [], marker='o', linestyle='', color=color)

    print("Renderer color =", color)
    print("Point_R color =", point_R.get_color())
    print("Point_M color =", point_M.get_color())

    trail_R, = ax.plot([], [], linestyle='-', color=color, linewidth=1.5)
    trail_M, = ax.plot([], [], linestyle='-', color=color, linewidth=1.5)

    total_frames = len(pos_R)

    # Reduce frames for faster animation
    max_display_frames = 400
    frame_step = max(1, total_frames // max_display_frames)
    frames = range(0, total_frames, frame_step)

    interval = playback_to_interval(playback_speed)

    def init():

        point_R.set_data([], [])
        point_M.set_data([], [])

        trail_R.set_data([], [])
        trail_M.set_data([], [])

        return point_R, point_M, trail_R, trail_M

    def update(frame):

        point_R.set_data([pos_R[frame, 0]], [pos_R[frame, 1]])
        point_M.set_data([pos_M[frame, 0]], [pos_M[frame, 1]])

        trail_R.set_data(pos_R[:frame+1, 0], pos_R[:frame+1, 1])
        trail_M.set_data(pos_M[:frame+1, 0], pos_M[:frame+1, 1])

        return point_R, point_M, trail_R, trail_M

    fig.ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames,
        init_func=init,
        interval=interval,
        blit=False
    )

    plt.show()