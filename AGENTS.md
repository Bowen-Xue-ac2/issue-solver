# Working on issue-solver

- This repository maintains a portable skill, not a service or scanner platform.
- Read `skills/issue-solver/SKILL.md` for the workbench's runtime behavior. Keep its
  references and report template inside that folder so copied installs work.
- Runtime reports and sensitive logs belong outside Git. `.issue-solver/` is
  ignored here; inspect staged files rather than relying on that rule alone.
- Helpers use Python 3.10+ standard library. Run `python3 -m unittest discover -s tests -v`
  for installer/discovery changes. For skill behavior, use the applicable scenarios
  in `examples/acceptance/README.md`; exercise copies in a temporary directory.
- Preserve existing installations, explicit destination selection, offline defaults,
  and the distinction between discovery and a successful scan/host activation.
- Do not vendor upstream skills without checking the actual pinned license and
  notices. Current optional sources are recorded in the skill's `references/sources.md`.
- Live server actions, remote scans, credentials and publishing require the user's
  applicable authorization. A test fixture grants access only to its local copy.
