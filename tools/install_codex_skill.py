"""Make this checkout's scanner discoverable to Codex without replacing skills."""

import argparse
from pathlib import Path


def install(destination):
    source = Path(__file__).resolve().parents[1] / ".agents/skills/vulnhunt-codex"
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError("scanner SKILL.md is missing")
    if destination.is_symlink() and destination.resolve() == source:
        return destination
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("destination already contains a different installation")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.symlink_to(source, target_is_directory=True)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path,
                        default=Path.home() / ".agents/skills/vulnhunt-codex")
    args = parser.parse_args()
    print(install(args.destination.expanduser().absolute()))


if __name__ == "__main__":
    main()
