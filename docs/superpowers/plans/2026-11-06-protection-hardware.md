# Protection and Hardware Increment Implementation Plan

> **For agentic workers:** This plan does not grant workflow activation. Execute task-by-task only using the method and stage explicitly authorized by the user. Skill references are dependencies within that scope, not permission to activate a full workflow. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two lightweight peer capabilities while preserving issue-solver 0.1.

**Architecture:** Extend the single portable entrypoint with two focused references,
conditional report fields and four synthetic offline examples. Keep the CLI intact.

**Tech Stack:** Markdown; existing Python 3.10+ standard-library installer.

**Spec:** [Incremental scope](../../scope.md#protection-and-hardware-increment).

## Global Constraints

- Continue `/workspace/issue-solver`, branch `codex/issue-solver-protection-hardware`,
  from `640da17870d1114df5755dd9b333d293c14fd9b5`; one writer, no merge/default-branch change.
- Preserve BowenX_WS and global Git settings; parent handles authorized push.
- No live scans/device tests, cleanup, repair, stress, firmware, elevation,
  security/network changes or credentials. Use synthetic reports only.
- Optional projects are pinned references, not bundled/installed dependencies.
- Apply user-enabled local SP A0/A18 and advisory STS; no hook enforcement claim.

## Review Focus

- Missing tools, stale definitions and partial/failed scans must not become clean.
- A quarantine match needs evidence before false-positive dismissal or restoration.
- SMART PASSED and short symptom-free intervals cannot prove hardware health/repair.
- Keep platform distinctions and operator/authorization boundaries in proposals.

### Task 1: Add and verify the two peer routes

**Files:** Modify `SKILL.md`, `assets/report.md`, `references/sources.md` inside
`skills/issue-solver/`; create `references/virus-protect.md` and `hardware.md`;
update `README.md`, `docs/scope.md`, `examples/scope.md`; add
`examples/protection-hardware/{README,av-incomplete,av-alert,storage,symptoms}.md`
and `docs/validation-protection-hardware.md`.

**Interfaces:** Existing `install --skills-dir DIR` copies the full skill; existing
`discover --skills-dir DIR` finds the same entrypoint. New routes consume supplied
OS-specific reports and produce evidence-bounded diagnosis/guidance through the
existing report template. No new executable interface or automatic action.

- [x] Observe pre-change independent retrieval coverage for both routes.
- [x] Verify GitHub candidate provenance, pinned licenses/versions, maintenance
      and dependencies; record selected and rejected references before adoption.
- [x] Add minimal route/reference/report changes and four harmless fixtures.
- [x] Install to a temporary directory, discover, compare package bytes and resolve
      relative references; expected: complete copy, valid links, same CLI shape.
- [x] Validate skill frontmatter with local `quick_validate.py`; expected: valid.
- [x] Run one independent forward consumer on all four fixtures using the installed
      package, then review the entire incremental diff. Inspect its actual reports.
- [x] Fix demonstrated gaps only, record affected verification, commit and hand off.

## Execution decisions

The user already requested autonomous research and implementation in this ongoing
task. The short plan records that authorized work without reopening design approval.
Existing separate checkout satisfies isolation; no new checkout is needed.
This is a reference increment: retrieval baseline and application scenarios are
the RED/GREEN method, not executable scanner tests or discipline wording trials.
Unchanged 0.1 CLI tests and five repair exercises retain their historical evidence.

Outcome and method evidence: [incremental validation](../../validation-protection-hardware.md).
Two source-precision corrections were included in the same review: smartctl ATA
bitmask applicability and nvme-cli platform-specific prerequisites. No runtime
code changed, no old repair fixtures were rerun, and no new review tier was added.
