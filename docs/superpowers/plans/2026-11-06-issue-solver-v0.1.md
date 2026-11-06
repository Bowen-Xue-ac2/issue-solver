# Issue Solver 0.1 Implementation Plan

> **For agentic workers:** This plan does not grant workflow activation. Execute task-by-task only using the method and stage explicitly authorized by the user. Skill references are dependencies within that scope, not permission to activate a full workflow. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Deliver the approved lightweight repair and authorized security workbench.

**Architecture:** One portable entry skill with focused references and a report
template. Python standard-library tooling only installs into an explicit local
directory and reports available local skills/tools; agents retain the reasoning.

**Tech Stack:** Markdown, Python 3.10+, unittest, Git.

**Spec:** [Approved scope](../../scope.md).

## Global Constraints

- Independent checkout and branch; no edits to other repositories or global config.
- No actual server scans, credential creation, network policy changes, or merge.
- No forced external installation; verify optional sources, licenses, immutable pins.
- No committed runtime logs; installation validation uses temporary directories.
- Apply local SP A0/A18 + advisory STS; reuse valid evidence and keep one writer.

## Review Focus

- An ordinary defect must not escalate into a broad security review.
- Installation must preserve existing skills and retain usable relative references.
- A failed or missing security tool must not become a clean security verdict.
- Confirmed flaws and false positives require local behavioral evidence.

### Task 1: Portable workbench and installation contract

**Files:** `README.md`, `AGENTS.md`, `skills/issue-solver/SKILL.md`,
`skills/issue-solver/references/{debugging,security,verification,sources}.md`,
`skills/issue-solver/assets/report.md`, `scripts/skills.py`, `tests/test_skills.py`.

**Interfaces:** `python3 scripts/skills.py install --skills-dir DIR` copies the
self-contained entry to `DIR/issue-solver`, refusing existing targets.
`discover --skills-dir DIR [--skills-dir DIR...]` prints JSON with readable
entrypoints, optional modules, and a Trivy PATH availability observation.
No helper command runs tools, installs dependencies, or reads project logs.

- [x] Write installation/discovery behavioral tests; run and observe missing CLI failure.
- [x] Observe a no-skill reference retrieval baseline before writing the entrypoint.
- [x] Implement copy/discovery and self-contained guidance; pin verified sources.
- [x] Run `python3 -m unittest discover -s tests -v`; expected all tests pass.
- [x] Commit the portable workbench and evidence-backed usage instructions.

### Task 2: Five-case forward acceptance and delivery

**Files:** `examples/acceptance/{README.md,app.py,ci.py,verify.py}`, `docs/validation.md`.

**Interfaces:** `python3 examples/acceptance/verify.py CASE --workspace DIR`
executes local fixture behavior for `bug`, `ci`, `security`, `false-positive`.
The missing-tool case consumes the real discovery command with an empty PATH.
Fixtures live only in a temporary copy during repair.

- [x] Add runnable exercises with independent assertions; observe three expected
      pre-fix failures and one already-safe case.
- [x] Install to a temporary skill root and run one independent consuming-agent
      forward test across all five cases; combine this with whole-branch review.
- [x] Repair only demonstrated acceptance defects; verify affected behavior.
- [x] Record concise sanitized validation, commit, and hand the verified branch
      to the parent for the already-authorized push; do not merge.

## Execution notes

The user already approved the scope and chose Astra implementation; this plan
records implementation decisions without reopening design approval. A separate
clone satisfies the explicitly requested isolation; no linked worktree is needed.
The reference skill is tested for retrieval and application, not as a new
discipline rule requiring repeated pressure/wording experiments.
