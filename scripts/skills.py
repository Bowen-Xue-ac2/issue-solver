#!/usr/bin/env python3
"""Offline installation and discovery only; never runs a skill or scanner."""

import argparse
import json
import os
from pathlib import Path
import shutil
import sys


NAMES = (
    "issue-solver",
    "debugging-strategies",
    "code-review",
    "property-based-testing",
    "security-best-practices",
    "security-threat-model",
)
SOURCE = Path(__file__).resolve().parents[1] / "skills" / "issue-solver"


def install(skills_dir):
    root = Path(skills_dir).expanduser().absolute()
    target = root / "issue-solver"
    if os.path.lexists(target):
        raise ValueError(f"Target already exists; nothing overwritten: {target}")
    if SOURCE.resolve() in target.resolve().parents:
        raise ValueError("Installation target must be outside the source skill directory")
    if not (SOURCE / "SKILL.md").is_file():
        raise ValueError(f"Source entrypoint is missing: {SOURCE / 'SKILL.md'}")
    root.mkdir(parents=True, exist_ok=True)
    # copytree also rejects an existing destination, including a concurrent install.
    shutil.copytree(SOURCE, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return {"status": "installed", "entrypoint": str(target / "SKILL.md")}


def discover(skills_dirs):
    roots = list(dict.fromkeys(Path(p).expanduser().absolute() for p in skills_dirs))
    found = {name: [] for name in NAMES}
    for root in roots:
        if root.exists() and not root.is_dir():
            raise ValueError(f"Skill root is not a directory: {root}")
        for name in NAMES:
            entry = root / name / "SKILL.md"
            if entry.is_file():
                # Observe readability, not YAML validity or host activation.
                with entry.open("rb") as stream:
                    stream.read(1)
                found[name].append(str(entry))
    trivy = shutil.which("trivy")
    return {
        "skills": found,
        "tools": {"trivy": {
            "status": "found-on-path" if trivy else "unavailable",
            "path": str(Path(trivy).absolute()) if trivy else None,
        }},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    install_parser = commands.add_parser("install", help="copy the skill; refuse existing target")
    install_parser.add_argument("--skills-dir", required=True, help="explicit destination skill root")
    discover_parser = commands.add_parser("discover", help="list known local entrypoints; no execution")
    discover_parser.add_argument("--skills-dir", required=True, action="append",
                                 help="directory directly containing skill folders; repeatable")
    args = parser.parse_args(argv)
    try:
        result = install(args.skills_dir) if args.command == "install" else discover(args.skills_dir)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
