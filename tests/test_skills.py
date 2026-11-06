"""Behavioral contract for the offline installer and capability discovery."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
CLI = REPO / "scripts" / "skills.py"


class SkillsCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="issue-solver-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skills = self.root / "skills with spaces"

    def run_cli(self, *args, path=None):
        env = os.environ.copy()
        if path is not None:
            env["PATH"] = str(path)
        return subprocess.run(
            [sys.executable, str(CLI), *map(str, args)],
            cwd=self.root, env=env, text=True, capture_output=True, timeout=10,
        )

    def test_install_is_portable_and_discoverable_from_another_cwd(self):
        result = self.run_cli("install", "--skills-dir", self.skills)
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = self.skills / "issue-solver"
        self.assertTrue((installed / "SKILL.md").is_file())
        self.assertTrue((installed / "references" / "security.md").is_file())
        self.assertTrue((installed / "assets" / "report.md").is_file())
        found = self.run_cli("discover", "--skills-dir", self.skills)
        self.assertEqual(found.returncode, 0, found.stderr)
        report = json.loads(found.stdout)
        self.assertEqual(report["skills"]["issue-solver"], [str(installed / "SKILL.md")])

    def test_existing_install_is_preserved(self):
        target = self.skills / "issue-solver"
        target.mkdir(parents=True)
        sentinel = target / "SKILL.md"
        sentinel.write_text("user maintained skill", encoding="utf-8")
        result = self.run_cli("install", "--skills-dir", self.skills)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sentinel.read_text(), "user maintained skill")
        self.assertEqual(list(target.iterdir()), [sentinel])

    def test_existing_symlink_is_preserved(self):
        real = self.root / "existing"
        real.mkdir()
        self.skills.mkdir()
        target = self.skills / "issue-solver"
        target.symlink_to(real, target_is_directory=True)
        result = self.run_cli("install", "--skills-dir", self.skills)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(target.is_symlink())
        self.assertEqual(list(real.iterdir()), [])

    def test_install_requires_an_explicit_root(self):
        result = self.run_cli("install")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_invalid_root_fails_without_traceback(self):
        self.skills.write_text("not a directory", encoding="utf-8")
        result = self.run_cli("install", "--skills-dir", self.skills)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.skills.read_text(), "not a directory")

    def test_missing_modules_and_tool_are_reported_without_installing(self):
        empty_path = self.root / "empty-path"
        empty_path.mkdir()
        result = self.run_cli("discover", "--skills-dir", self.skills, path=empty_path)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["skills"]["issue-solver"], [])
        self.assertEqual(report["skills"]["security-best-practices"], [])
        self.assertEqual(report["tools"]["trivy"], {"status": "unavailable", "path": None})
        self.assertFalse(self.skills.exists())
        self.assertEqual(list(empty_path.iterdir()), [])

    def test_discovery_keeps_multiple_candidates_and_does_not_execute_tools(self):
        second = self.root / "second"
        for root in (self.skills, second):
            module = root / "code-review"
            module.mkdir(parents=True)
            (module / "SKILL.md").write_text("---\nname: code-review\n---\n", encoding="utf-8")
        binary_dir = self.root / "bin"
        binary_dir.mkdir()
        binary = binary_dir / "trivy"
        marker = self.root / "was-executed"
        binary.write_text(f"#!/bin/sh\ntouch '{marker}'\n", encoding="utf-8")
        binary.chmod(0o755)
        result = self.run_cli("discover", "--skills-dir", self.skills,
                              "--skills-dir", second, path=binary_dir)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(len(report["skills"]["code-review"]), 2)
        self.assertEqual(report["tools"]["trivy"], {"status": "found-on-path", "path": str(binary)})
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
