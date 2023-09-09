import subprocess
from pathlib import Path

import kumade as ku

project_dir = Path(__file__).parent
doc_src = project_dir / "sphinx"
doc_dst = project_dir / "docs"

@ku.task("format")
@ku.help("Format code by pysen.")
def format() -> None:
    subprocess.run(["pysen", "run", "format"])

@ku.task("lint")
@ku.help("Lint code by pysen.")
def lint() -> None:
    subprocess.run(["pysen", "run", "lint"])

@ku.task("doc")
@ku.help("Build document.")
def doc() -> None:
    subprocess.run(["sphinx-build", str(doc_src), str(doc_dst)])
