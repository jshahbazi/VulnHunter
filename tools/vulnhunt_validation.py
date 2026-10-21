"""Generate synthetic scanner cases and independently check their behavior.

Outputs belong in an ignored/private directory. This is a smoke corpus, not a
measurement of security recall on production code. Python standard library only.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile


CASES = {
    "case-a": '''from pathlib import Path

def read_resource(root, resource):
    """Serve an unauthenticated caller-selected resource under root."""
    return (Path(root) / resource).read_text()
''',
    "case-b": '''from pathlib import Path

def read_resource(root, resource):
    """Serve an unauthenticated caller-selected resource under root."""
    base = Path(root).resolve()
    candidate = (base / resource).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError("outside resource root")
    return candidate.read_text()
''',
    "case-c": '''import subprocess

def format_name(name):
    """Format an unauthenticated caller-supplied display name."""
    return subprocess.run("printf '%s' " + name, shell=True,
                          check=True, capture_output=True, text=True).stdout
''',
    "case-d": '''import subprocess

def format_name(name):
    """Format an unauthenticated caller-supplied display name."""
    return subprocess.run(["printf", "%s", name], shell=False,
                          check=True, capture_output=True, text=True).stdout
''',
}


def generate(destination):
    destination.mkdir(parents=True, exist_ok=False)
    hashes = {}
    for name, source in CASES.items():
        case = destination / name
        case.mkdir()
        (case / "app.py").write_text(source)
        hashes[name] = hashlib.sha256(source.encode()).hexdigest()
    return hashes


def check(destination):
    modules = {}
    for name, source in CASES.items():
        path = destination / name / "app.py"
        if path.read_text() != source:
            raise ValueError("fixture source changed")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules[name] = module
    with tempfile.TemporaryDirectory(prefix="vulnhunt-oracle-") as scratch:
        base = Path(scratch)
        resources = base / "resources"
        resources.mkdir()
        (resources / "allowed.txt").write_text("allowed")
        (base / "outside.txt").write_text("synthetic outside resource")
        for name in ("case-a", "case-b"):
            assert modules[name].read_resource(resources, "allowed.txt") == "allowed"
        assert modules["case-a"].read_resource(resources, "../outside.txt") == "synthetic outside resource"
        try:
            modules["case-b"].read_resource(resources, "../outside.txt")
        except ValueError:
            pass
        else:
            raise AssertionError("containment check failed")
        for name in ("case-c", "case-d"):
            assert modules[name].format_name("hello") == "hello"
            marker = base / (name + "-marker")
            payload = "hello; printf marker > " + str(marker)
            result = modules[name].format_name(payload)
            if name == "case-c":
                assert marker.read_text() == "marker"
            else:
                assert not marker.exists()
                assert result == payload
    return {"cases": 4, "positive_cases": 2, "negative_cases": 2,
            "behavior_checks": "passed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("generate", "check"))
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    result = generate(args.destination) if args.mode == "generate" else check(args.destination)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
