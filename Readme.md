This project plots the paths of two electrons as one approaches the other.
As the simulation begins:
- Electron R starts out "at rest."
- Electron M is moving from left to right at constant velocity.
- If there were no electromagnetic forces, M would pass R at an offset.
The user can specify a number of runs of the simulation with different starting velocities and offsets for M by specifyin VELOCITIES and IMPACT_PARAMETERS in the file config.py. For example two runs at 30% and 60% of the speed of light run with an offset of 5 would be specified like this:
VELOCITIES = [
    30,60
]

IMPACT_PARAMETERS = [
    5
]
The impact parameters are dimensionless.

Run the simulation(s) by executing run.sh
In a terminal change to the ElectronSimulation directory and type ./run.sh. In a file explorer GUI like Nautilus, right click on run.sh and select Run as Program.

The calculations are all done first, then plotted. This can take some time, so be patient.
