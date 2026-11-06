# issue-solver 0.1 scope

A portable skill workbench for a bounded issue, CI failure, code defect,
security alert, or an explicitly authorized server-configuration question.
The common path is scope/routing → evidence/reproduction → minimal repair →
targeted verification → delivery. A normal bug does not trigger a security audit.

The entrypoint selects debugging, ordinary review, or algorithm/boundary
properties as needed. Security work adds best-practice checks, attack-path
reasoning, false-positive checks, differential review, or a requested threat
model only when relevant. Prefer installed capabilities; optional references
have immutable source pins and verified licenses. No third-party skill text is
vendored and no network installation is required.

This release provides instructions, references, examples, a report template,
and a standard-library helper for explicit local installation and discovery.
It has no issue executor, scanner wrapper, database, queue, background service,
automatic remediation, or network configuration. Trivy is optional; Lynis,
remote servers, and offensive tests remain scoped authorization interfaces.
Runtime reports, source snapshots, and sensitive logs are not release content.

Acceptance: an isolated local consumer can install/discover the skill and use
it on an ordinary bug, CI failure, confirmed security flaw, false positive,
and unavailable optional tool. Tests must observe behavior, not merely find
words in Markdown. Publish on a separate branch; do not merge.

