from __future__ import annotations

from pathlib import Path
from shutil import rmtree


def main() -> None:
    for path in Path.cwd().rglob("__pycache__"):
        rmtree(path)


if __name__ == "__main__":
    main()
