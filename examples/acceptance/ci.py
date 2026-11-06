"""Intentional cwd-dependent CI failure; run only as a local exercise."""

import json
from pathlib import Path


def check():
    return json.loads(Path("config.json").read_text(encoding="utf-8"))["status"]


if __name__ == "__main__":
    print(check())
