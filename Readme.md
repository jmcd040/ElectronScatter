# Readme.md version 3.02

## Purpose

This project plots the paths of two electrons as one approaches the other.
As the simulation begins:

- Electron R is assumed to be "at rest."
- Electron M is moving from left to right across the plot at constant velocity.
- If there were no electromagnetic forces, M would pass R at an offset called the IMPACT_PARAMETER. The distances and physics constants are in a normalized system. That means that the actual distance of the IMPACT_PARAMETER is not in, say MKS.

## Environment

This has been tested on Ubuntu 24 with Python3
The program will install a virtual environment (venv) if it isn't installed, then it will load the numpy and matplolib python libraries.
To prove the entire environment is valid, the program will make a test plot. When it appears, close the window, then the actual plot will be computed and displayed. Once you are sure this is working, this test plot can be disabled in config.py

## User Input

The user can specify a number of runs of the simulation with different starting velocities and offsets for M by specifying VELOCITIES and IMPACT_PARAMETERS in the file config.py. For example two runs at 30% and 60% of the speed of light run with an offset of 5 would be specified like this:
VELOCITIES = [
    30,60
]

IMPACT_PARAMETERS = [
    5
]
The impact parameters are dimensionless.

## Starting the Simulation

Run the simulation(s) by executing `run.sh`.
To run in a terminal window, open the terminal, change to the ElectronScatter directory and type `./run.sh`.
In a file explorer GUI like Nautilus, right click on run.sh and select Run as Program. (First make sure run.sh is executable.)

The calculations are all done first, then plotted.

Close the plot before running again.
