#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
import venv

PROJECT_DIR = Path(__file__).resolve().parent
VENV_DIR = PROJECT_DIR / "venv"
REQUIREMENTS_FILE = PROJECT_DIR / "requirements.txt"


def run(cmd):
    subprocess.check_call(cmd)


def venv_python():
    return VENV_DIR / "bin" / "python"


def ensure_venv():
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)

def ensure_packages(py):
    if not REQUIREMENTS_FILE.exists():
        print("requirements.txt not found — skipping dependency install")
        return

    print("Installing / verifying dependencies from requirements.txt...")

    run([
        py,
        "-m",
        "pip",
        "install",
        "-r",
        str(REQUIREMENTS_FILE)
    ])


def run_gui_test(py):
    try:
        import config
    except Exception:
        return

    if not getattr(config, "RUN_ENVIRONMENT_GUI_TEST", True):
        return

    print("Running matplotlib GUI test...")

    run([
        py,
        "-c",
        (
            "import matplotlib.pyplot as plt;"
            "plt.plot([1,2,3]);"
            "plt.title('ElectronScatter environment test');"
            "plt.show()"
        )
    ])


def main():
    ensure_venv()

    py = str(venv_python())

    ensure_packages(py)

    run_gui_test(py)


if __name__ == "__main__":
    main()