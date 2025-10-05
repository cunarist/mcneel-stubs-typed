"""
This script is intended to be run on Windows
where `PyStubbler.exe` is available in `builder/bin`.
"""

import subprocess
from pathlib import Path
from typing import NamedTuple, Optional

ROOT_DIR = Path(__file__).parent.parent
RHINO_BASE = Path("C:\\") / "Program Files" / "Rhino 8"


class AssemblyPlan(NamedTuple):
    dest_sub: str
    assembly_path: Path


def build_commands() -> list[list[str]]:
    """
    Build the list of commands to run,
    each command as a list of argv parts.
    """
    # Paths derived from the Rhino base
    rhino_plugins = RHINO_BASE / "Plug-ins"
    rhino_system = RHINO_BASE / "System"

    # Location of the PyStubbler executable inside the repo
    builder_bin = ROOT_DIR / "builder" / "bin"
    py_stubbler = builder_bin / "PyStubbler.exe"

    # Check if PyStubbler exists
    if not py_stubbler.exists():
        raise FileNotFoundError("Please compile PyStubbler with Visual Studio first")

    # Verify common assembly locations
    targets: list[AssemblyPlan] = [
        AssemblyPlan("Eto", rhino_system / "Eto.dll"),
        AssemblyPlan("Rhino", rhino_system / "RhinoCommon.dll"),
        AssemblyPlan("Grasshopper", rhino_plugins / "Grasshopper" / "Grasshopper.dll"),
        AssemblyPlan("GH_IO", rhino_plugins / "Grasshopper" / "GH_IO.dll"),
        AssemblyPlan("GH_Util", rhino_plugins / "Grasshopper" / "GH_Util.dll"),
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


def main(argv: Optional[list[str]] = None):
    """
    Main entrypoint.
    """

    # Get the directory of PyStubbler.exe
    builder_bin = ROOT_DIR / "builder" / "bin"

    # Build the commands list
    commands = build_commands()

    # Run each command
    for argv in commands:
        subprocess.run(argv, cwd=builder_bin, check=True)


if __name__ == "__main__":
    main()
