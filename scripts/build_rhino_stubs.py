"""Build Rhino stubs using PyStubbler on Windows.

Run this script on Windows where `PyStubbler.exe` is available in `builder/bin`.
"""

import subprocess
from pathlib import Path
from typing import NamedTuple

ROOT_DIR = Path(__file__).parent.parent
RHINO_BASE = Path("C:\\") / "Program Files" / "Rhino 8"


class GenPlan(NamedTuple):
    """Generation plan for building stubs from an assembly."""

    dest_sub: str
    assembly_path: Path


def build_commands() -> list[list[str]]:
    """Build the list of commands to run.

    Each command is returned as a list of argv parts.
    """
    # Paths derived from the Rhino base
    rhino_plugins = RHINO_BASE / "Plug-ins"
    rhino_system = RHINO_BASE / "System"

    # Location of the PyStubbler executable inside the repo
    builder_bin = ROOT_DIR / "builder" / "bin"
    py_stubbler = builder_bin / "PyStubbler.exe"

    # Check if PyStubbler exists
    if not py_stubbler.exists():
        msg = "Please compile PyStubbler with Visual Studio first"
        raise FileNotFoundError(msg)

    # Verify common assembly locations
    targets: list[GenPlan] = [
        GenPlan("Eto", rhino_system / "Eto.dll"),
        GenPlan("Rhino", rhino_system / "RhinoCommon.dll"),
        GenPlan("Grasshopper", rhino_plugins / "Grasshopper" / "Grasshopper.dll"),
        GenPlan("GH_IO", rhino_plugins / "Grasshopper" / "GH_IO.dll"),
        GenPlan("GH_Util", rhino_plugins / "Grasshopper" / "GH_Util.dll"),
    ]

    commands: list[list[str]] = []

    for dest_sub, assembly_path in targets:
        dest_path = str(ROOT_DIR / "stubs" / dest_sub)
        command = [
            str(py_stubbler),
            f"--dest={dest_path}",
            f"--search={rhino_system.resolve()}",
            str(assembly_path.resolve()),
        ]
        commands.append(command)

    return commands


def main() -> None:
    """Run PyStubbler to generate stubs for all Rhino assemblies."""
    # Get the directory of PyStubbler.exe
    builder_bin = ROOT_DIR / "builder" / "bin"

    # Build the commands list
    commands = build_commands()

    # Run each command
    for cmd in commands:
        subprocess.run(cmd, cwd=builder_bin, check=True)


if __name__ == "__main__":
    main()
