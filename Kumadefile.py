import subprocess
from pathlib import Path

import kumade as ku


@ku.task("format")
@ku.help("Format code by pysen.")
def format() -> None:
    subprocess.run(["pysen", "run", "format"])

@ku.task("lint")
@ku.help("Lint code by pysen.")
def lint() -> None:
    subprocess.run(["pysen", "run", "lint"])
