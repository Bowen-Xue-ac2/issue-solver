"""Independent acceptance assertions; edit the workspace copy, not this verifier."""

import argparse
import importlib.util
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest


def load_app(workspace):
    spec = importlib.util.spec_from_file_location("exercise_app", workspace / "app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BugCase(unittest.TestCase):
    def test_preserves_values_and_chunk_bounds(self):
        app = load_app(WORKSPACE)
        for length in range(21):
            for size in range(1, 9):
                with self.subTest(length=length, size=size):
                    values = list(range(length))
                    chunks = app.batches(values, size)
                    self.assertEqual([v for chunk in chunks for v in chunk], values)
                    self.assertTrue(all(0 < len(chunk) <= size for chunk in chunks))

    def test_rejects_nonpositive_sizes(self):
        app = load_app(WORKSPACE)
        for size in (0, -1):
            with self.subTest(size=size), self.assertRaises(ValueError):
                app.batches([1], size)


class CICase(unittest.TestCase):
    def test_runner_cwd_is_not_required_to_contain_the_config(self):
        with tempfile.TemporaryDirectory(prefix="issue-solver-runner-") as cwd:
            result = subprocess.run(
                [sys.executable, str(WORKSPACE / "ci.py")], cwd=cwd,
                capture_output=True, text=True, timeout=10,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "ready")


class QueryContract(unittest.TestCase):
    function = "lookup_reported"

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.addCleanup(self.connection.close)
        self.connection.execute("CREATE TABLE products (name TEXT, price INTEGER)")
        self.connection.executemany("INSERT INTO products VALUES (?, ?)",
                                    [("tea", 5), ("O'Reilly", 12)])
        self.lookup = getattr(load_app(WORKSPACE), self.function)

    def test_injection_remains_literal(self):
        self.assertEqual(self.lookup(self.connection, "' OR 1=1 --"), [])

    def test_quoted_legitimate_value_is_preserved(self):
        self.assertEqual(self.lookup(self.connection, "O'Reilly"), [(12,)])

    def test_regular_lookup_still_works(self):
        self.assertEqual(self.lookup(self.connection, "tea"), [(5,)])


class FalsePositiveCase(QueryContract):
    function = "lookup_bound"


CASES = {"bug": BugCase, "ci": CICase, "security": QueryContract,
         "false-positive": FalsePositiveCase}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=(*CASES, "all"))
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    WORKSPACE = args.workspace.resolve()
    chosen = CASES.values() if args.case == "all" else [CASES[args.case]]
    suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(c) for c in chosen)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
